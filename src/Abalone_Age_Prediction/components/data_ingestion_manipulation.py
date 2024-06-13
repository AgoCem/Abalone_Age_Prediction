import urllib.request as request
from Abalone_Age_Prediction.utils.common import save_data
from Abalone_Age_Prediction import logger
from Abalone_Age_Prediction.entity.config_entity import DataIngestionManipulationConfig
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from pathlib import Path
import pandas as pd
import os


class DataIngestionManipulation:
    def __init__(self, config: DataIngestionManipulationConfig):
        self.config = config

    def download_file(self):
        """
        file_path: str
        Download, if it doesn't already exists, the csv file with data, don't need a return, just to save the Data
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename= self.config.local_data_file
            )

            #logger.info(f"{filename} is downloading with the following info: \n{headers}")
        else:
            logger.info(f"File already downloaded")
        
        return None
    
    def read_file(self):
        """
        Read the csv file
        """
        try:
            
            df = pd.read_csv(self.config.local_data_file)

            return df

        except Exception as e:
            e

    def preprocess_file(self,df):
        """
        Preprocess the data and save it into a training and testing files
        I don't need a return, i just need to save the training and testing data
        """

        numerical_cols = df.select_dtypes(include='number').columns
        categorical_cols = df.select_dtypes(include='object').columns

        

        for col in categorical_cols:
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])

        X = df.drop(labels = self.config.target_col, axis = 1)
        y = df[self.config.target_col]
        
        scaler = MinMaxScaler()
        numerical_cols = numerical_cols.drop(self.config.target_col)
        X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=10)

        train_data = pd.concat([X_train,y_train])
        test_data = pd.concat([X_test,y_test])

        training_path = self.config.save_training_file
        #print("Before")
        save_data(Path(training_path),train_data,"train.csv")
        #print("After")
        save_data(Path(training_path),test_data,"test.csv")
        
        return None
    