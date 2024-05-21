import joblib
from utils.data_loader import load_data
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, mean_absolute_error
import numpy as np

def evaluate_model(test_path=None, from_db=False):
    _, test = load_data(test_path=test_path, from_db=from_db)
    pipeline = joblib.load('model/model.joblib')
    target_col = "price"
    
    test_predictions = pipeline.predict(test.drop(columns=[target_col]))
    test_target = test[target_col].values
    
    rmse = np.sqrt(mean_squared_error(test_target, test_predictions))
    mape = mean_absolute_percentage_error(test_target, test_predictions)
    mae = mean_absolute_error(test_target, test_predictions)
    
    print(f"RMSE: {rmse}")
    print(f"MAPE: {mape}")
    print(f"MAE: {mae}")

if __name__ == "__main__":
    # Set `from_db=True` if you want to load data from the database
    evaluate_model(test_path='data/test.csv', from_db=False)
