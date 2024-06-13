from Abalone_Age_Prediction.utils.common import create_directories, read_yaml
from Abalone_Age_Prediction.constants import *
from Abalone_Age_Prediction.entity.config_entity import DataIngestionManipulationConfig



class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root]) #the artifacts_root is the key of the dictionary created
                                                # in the yaml file and we can read this key like that instead of
                                                # ["artifacts_root"] because we used the ConfigBox in the common.py file


    def get_data_ingestion_config(self) -> DataIngestionManipulationConfig:
        config = self.config.data_ingestion_manipulation #data ingestion is the other key value of the dictionary in the config.yaml file

        create_directories([config.root_dir,config.save_training_file])

        data_ingestion_manipulation_config = DataIngestionManipulationConfig(
            root_dir=config.root_dir,
            local_data_file = config.local_data_file,
            source_URL = config.source_URL,
            save_training_file= config.save_training_file,
            target_col=self.params.TARGET
        )                                     

        return data_ingestion_manipulation_config