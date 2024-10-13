from MLRegression import logger
from MLRegression.pipeline.stage_01_data_ingection import DataIngestionTrainingPipeline
from MLRegression.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MLRegression.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MLRegression.pipeline.stage_04_model_trainer_rf import ModelTrainerTrainingPipeline
from MLRegression.pipeline.stage_05_model_evaluation_rf import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Validation stage"
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      obj = DataValidationTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e


STAGE_NAME = "Data Transformation stage"
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      obj = DataTransformationTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e

# STAGE_NAME = "Model Trainer stage"
# try:
#       logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#       obj = ModelTrainerTrainingPipeline()
#       obj.main()
#       logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#       logger.exception(e)
#       raise e

STAGE_NAME = "Model Trainer stage using RF"
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      obj = ModelTrainerTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e

STAGE_NAME = "Model Evaluation stage using RF"
try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      obj = ModelEvaluationTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
