from Abalone_Age_Prediction.config.configuration import ConfigurationManager
from Abalone_Age_Prediction.components.model_evaluation import ModelEvaluation
from Abalone_Age_Prediction import logger



STAGE_NAME = "Model Evaluation"


class ModelEvaluationPipeline:
    def __init__(self):
        pass



    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        testing_data = model_evaluation.read_file()
        model_evaluation.model_evaluation(testing_data)




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e