# deploy_model.py

import joblib
import os

def deploy(model, deploy_path):
    '''
    Function to deploy the trained model to a specified path.
    
    Args:
    model: Trained model.
    deploy_path (str): Path where the model will be deployed.
    '''
    # Ensure the directory exists
    os.makedirs(os.path.dirname(deploy_path), exist_ok=True)
    
    # Save the model
    joblib.dump(model, deploy_path)
    
    print(f"Model deployed successfully at {deploy_path}")
