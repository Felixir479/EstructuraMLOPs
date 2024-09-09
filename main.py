# main.py

from config.config import Config
from src.data.load_data import load_data_from_sql, get_sql_connection
from src.data.process_data import process_data
from src.models.train_model import train_model
from src.deploy.deploy_model import deploy
from src.utils.logging_utils import setup_logging, log_info

def main():
    setup_logging()

    log_info("Starting main execution flow...")
    
    # Load configuration
    config = Config()
    
    # Load and process data
    connection = get_sql_connection(config.db_connection_string)
    data = load_data_from_sql(connection, config.query)
    X_train, X_test, y_train, y_test = process_data(data)
    
    # Train model
    model = train_model(X_train, y_train, config.model_params)
    
    # Deploy model
    deploy(model, config.deploy_path)
    
    log_info("Execution flow completed successfully.")

if __name__ == "__main__":
    main()
