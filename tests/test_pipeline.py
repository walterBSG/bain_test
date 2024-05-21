import unittest
import pandas as pd
from utils.data_loader import load_data
from model.pipeline import build_pipeline

class TestPipeline(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Load data once for all tests
        cls.train, cls.test = load_data('data/train.csv', 'data/test.csv')
        cls.categorical_cols = ["type", "sector"]
        cls.target_col = "price"
        cls.pipeline = build_pipeline(cls.categorical_cols, cls.target_col)
    
    def test_pipeline_fit(self):
        # Test if pipeline can fit the model
        self.pipeline.fit(self.train.drop(columns=['id', self.target_col]), self.train[self.target_col])
        self.assertTrue(hasattr(self.pipeline, 'predict'), "Pipeline does not have a predict method after fitting.")
    
    def test_pipeline_predict(self):
        # Ensure the model can make predictions
        self.pipeline.fit(self.train.drop(columns=['id', self.target_col]), self.train[self.target_col])
        predictions = self.pipeline.predict(self.test.drop(columns=['id', self.target_col]))
        self.assertEqual(len(predictions), len(self.test), "Number of predictions does not match number of test samples.")
    
    def test_pipeline_output_range(self):
        # Check that predictions are within a reasonable range (optional based on your dataset)
        self.pipeline.fit(self.train.drop(columns=['id', self.target_col]), self.train[self.target_col])
        predictions = self.pipeline.predict(self.test.drop(columns=['id', self.target_col]))
        self.assertTrue((predictions >= 0).all(), "Some predictions are negative.")
    
    def test_pipeline_with_partial_fit(self):
        # Test if the pipeline can be updated with new data
        self.pipeline.fit(self.train.drop(columns=['id', self.target_col]), self.train[self.target_col])
        new_data = self.train.sample(frac=0.1)
        self.pipeline.fit(new_data.drop(columns=['id', self.target_col]), new_data[self.target_col])
        self.assertTrue(hasattr(self.pipeline, 'predict'), "Pipeline does not have a predict method after refitting with new data.")

if __name__ == "__main__":
    unittest.main()
