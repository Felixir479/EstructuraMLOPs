# test_train_model.py

import unittest
from src.models.train_model import train_model
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

class TestTrainModel(unittest.TestCase):

    def setUp(self):
        # Create a synthetic dataset
        self.X, self.y = make_classification(n_samples=100, n_features=20, random_state=42)
        self.model_params = {"n_estimators": 10, "max_depth": 5, "random_state": 42}

    def test_train_model(self):
        model = train_model(self.X, self.y, self.model_params)
        self.assertIsInstance(model, RandomForestClassifier)
        self.assertEqual(len(model.estimators_), self.model_params['n_estimators'])

if __name__ == '__main__':
    unittest.main()
