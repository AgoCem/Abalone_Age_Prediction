from Abalone_Age_Prediction import logger
from Abalone_Age_Prediction.pipeline.stage_01_data_ingestion_manipulation import DataIngestionManipulationPipeline
from Abalone_Age_Prediction.pipeline.stage_02_model_preparation_and_validation import ModelPreparationValidationPipeline




STAGE_NAME = "Data Ingestion and Manipulation"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion_manipulation = DataIngestionManipulationPipeline()
   data_ingestion_manipulation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e



STAGE_NAME = "Model Preparation and Validation"


try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_preparation_validation = ModelPreparationValidationPipeline()
   model_preparation_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e