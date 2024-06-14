from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.svm import SVR
from Abalone_Age_Prediction.utils.common import save_object
from pathlib import Path
import pandas as pd
from Abalone_Age_Prediction.config.configuration import ModelPreparationTrainingConfig



class ModelPreparationTraining:
    def __init__(self, config: ModelPreparationTrainingConfig):
        self.config = config

    
    
    def read_file(self):
        """
        Read the csv file
        """
        try:
            
            training_data = pd.read_csv(self.config.local_data_file)

            return training_data

        except Exception as e:
            e

    def model_preparation_training(self,training_data):
        """
        Prepare the data and the model, and then train and save the trained models
        """
        X_train = training_data.drop(labels = self.config.param_target_col, axis = 1)
        y_train = training_data[self.config.param_target_col]

        rfr = RandomForestRegressor(n_estimators=self.config.param_n_estim_rfr, random_state=self.config.param_random_state)
        rfr.fit(X_train,y_train)
        svr = SVR(C=self.config.param_c_svr)
        svr.fit(X_train,y_train)
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        lasso = Lasso(alpha=self.config.param_alpha_lasso)
        lasso.fit(X_train,y_train)
        ridge = Ridge(alpha=self.config.param_alpha_ridge)
        ridge.fit(X_train,y_train)
        elastic = ElasticNet(alpha=self.config.param_alpha_elastic, l1_ratio=self.config.param_l1_elastic)
        elastic.fit(X_train,y_train)

        rfr_pkl = "rfr.pkl"
        svr_pkl = "svr.pkl"
        lr_pkl = "lr.pkl"
        lasso_pkl = "lasso.pkl"
        ridge_pkl = "ridge.pkl"
        elastic_pkl = "elastic.pkl"

        save_object(Path(self.config.trained_model_path),rfr,rfr_pkl)
        save_object(Path(self.config.trained_model_path),svr,svr_pkl)
        save_object(Path(self.config.trained_model_path),lr,lr_pkl)
        save_object(Path(self.config.trained_model_path),lasso,lasso_pkl)
        save_object(Path(self.config.trained_model_path),ridge,ridge_pkl)
        save_object(Path(self.config.trained_model_path),elastic,elastic_pkl)
        
        return None
    