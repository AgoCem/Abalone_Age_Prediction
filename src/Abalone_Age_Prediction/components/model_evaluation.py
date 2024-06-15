import pandas as pd
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from Abalone_Age_Prediction import logger
from Abalone_Age_Prediction.utils.common import load_object, save_object
from pathlib import Path
from Abalone_Age_Prediction.config.configuration import ModelEvaluationConfig




class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    
    def read_file(self):
        """
        Read the csv file
        """
        try:
            
            testing_data = pd.read_csv(self.config.local_data_file)

            return testing_data

        except Exception as e:
            e

    
    def evaluation_metrics(self,X_test,y_test, models: dict):
        """
        Evaluate all the models and returns 3 dictionaries with the different evaluation scores
        """
        r2_dic = {}
        mse_dic = {}
        mae_dic = {}
    

        for key in models.keys():
            r2_val =  r2_score(y_test,models[key].predict(X_test))
            mse_val = mean_squared_error(y_test,models[key].predict(X_test))
            mae_val = mean_absolute_error(y_test,models[key].predict(X_test))
            r2_dic[key] = r2_val
            mse_dic[key] = mse_val
            mae_dic[key] = mae_val
        return r2_dic, mse_dic, mae_dic


        


    def model_evaluation(self,testing_data):
        """
        Loading the data and the models and evaluate them
        """
        X_test = testing_data.drop(labels = self.config.param_target_col, axis = 1)
        y_test = testing_data[self.config.param_target_col]

        models = {
            "elastic" : load_object(Path(self.config.elastic_pickle)),
            "lasso" : load_object(Path(self.config.lasso_pickle)),
            "lr" : load_object(Path(self.config.lr_pickle)),
            "rfr" : load_object(Path(self.config.rfr_pickle)),
            "ridge" : load_object(Path(self.config.ridge_pickle)),
            "svr" : load_object(Path(self.config.svr_pickle))
        }

        r2_dic, mse_dic, mae_dic = self.evaluation_metrics(X_test,y_test,models)

        best_model = [i for i in r2_dic if r2_dic[i]==max(r2_dic.values())]
        best_model_score = max(r2_dic.values())
        
        logger.info(f"R2 Score dictionary : {r2_dic} \n")
        logger.info(f"MSE dictionary : {mse_dic} \n")
        logger.info(f"MAE Score dictionary : {mae_dic} \n")
        logger.info(f"The best model is {best_model[0]} with {round(best_model_score,3)} R2 score")

        save_object(Path(self.config.best_model_path), models[best_model[0]],"best_model.pkl")
        
        return None