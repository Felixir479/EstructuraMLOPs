# train_model.py

from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X_train, y_train, model_params):
    '''
    Function to train a model using the provided data and parameters.
    
    Args:
    X_train: Features of the training set.
    y_train: Labels of the training set.
    model_params (dict): Parameters for the model.
    
    Returns:
    Trained model.
    '''
    # Initialize the model with given parameters
    model = RandomForestClassifier(**model_params)
    
    # Train the model
    model.fit(X_train, y_train)
    
    return model

def save_model(model, path):
    '''
    Save the trained model to a file.
    
    Args:
    model: Trained model.
    path (str): Path to save the model.
    '''
    joblib.dump(model, path)
