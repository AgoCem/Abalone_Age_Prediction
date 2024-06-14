from Abalone_Age_Prediction.config.configuration import ConfigurationManager
from Abalone_Age_Prediction.components.model_preparation_and_training import ModelPreparationTraining
from Abalone_Age_Prediction import logger



STAGE_NAME = "Model Preparation and Validation"


class ModelPreparationValidationPipeline:
    def __init__(self):
        pass



    def main(self):
        config = ConfigurationManager()
        model_preparation_training_config = config.get_model_preparation_training_config()
        model_preparation_training = ModelPreparationTraining(config=model_preparation_training_config)
        training_data = model_preparation_training.read_file()
        model_preparation_training.model_preparation_training(training_data)




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelPreparationValidationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e