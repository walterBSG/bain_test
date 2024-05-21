import pandas as pd
from utils.db_utils import read_data_from_db

def load_data(train_path: str = None, test_path: str = None, from_db: bool = False):
    if from_db:
        train_query = "SELECT * FROM train_data"
        test_query = "SELECT * FROM test_data"
        train = read_data_from_db(train_query)
        test = read_data_from_db(test_query)
    else:
        train = pd.read_csv(train_path)
        test = pd.read_csv(test_path)
    return train, test
