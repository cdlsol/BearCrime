import time
import pandas as pd
from loguru import logger

def get_csv_data():

    try:
        start_time = time.time()

        logger.info("Extracting data from csv")

        df = pd.read_csv("./bearattack.csv")

        elapsed_time = time.time() - start_time

        logger.info(f"Data extracted in {elapsed_time:.2f} seconds")

        return df   

    except Exception as e:
        logger.error(f"Error extracting data: {e}")
        raise