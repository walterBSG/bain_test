import joblib
from utils.data_loader import load_data
from model.pipeline import build_pipeline

def train_model(train_path=None, test_path=None, from_db=False):
    train, test = load_data(train_path, test_path, from_db=from_db)
    
    categorical_cols = ["type", "sector"]
    numeric_cols = ["net_usable_area", "net_area", "n_rooms", "n_bathroom", "latitude", "longitude"]
    target_col = "price"
    
    pipeline = build_pipeline(categorical_cols, numeric_cols, target_col)
    pipeline.fit(train.drop(columns=[target_col]), train[target_col])
    
    joblib.dump(pipeline, 'model/model.joblib')

if __name__ == "__main__":
    # Set `from_db=True` if you want to load data from the database
    train_model(train_path='data/train.csv', test_path='data/test.csv', from_db=False)
