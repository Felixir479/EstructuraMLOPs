# retrain_model.py

from config.config import Config
from src.data.load_data import load_data_from_sql, get_sql_connection
from src.data.process_data import process_data
from src.models.train_model import train_model, save_model
from src.utils.logging_utils import setup_logging, log_info

def retrain_model():
    """
    Script to retrain the model with new data.
    """
    setup_logging()

    log_info("Starting model retraining process...")
    
    # Load configuration
    config = Config()
    
    # Load and process data
    connection = get_sql_connection(config.db_connection_string)
    data = load_data_from_sql(connection, config.query)
    X_train, X_test, y_train, y_test = process_data(data)
    
    # Train model
    model = train_model(X_train, y_train, config.model_params)
    
    # Save the new model
    save_model(model, config.deploy_path)
    
    log_info("Model retraining completed and model saved successfully.")

if __name__ == "__main__":
    retrain_model()
