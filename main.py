from sensor.exception import SensorException
from sensor.logger import logging
import os
import sys
#from sensor.utils import dump_to_mongodb
import certifi
from sensor.pipeline.training_pipeline import TrainPipeline
ca=certifi.where()



# def test_exception():
#     try:
#         logging.info("division by zero error")
#         a=1/0
#     except Exception as e:
#         raise SensorException(e,sys)
    
if __name__=="__main__":
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)
    # file_path="aps_failure_training_set1.csv"
    # database_name="db1"
    # collection_name="sensor"
    # dump_to_mongodb(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()

        