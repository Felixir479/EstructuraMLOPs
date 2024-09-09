# logging_utils.py

import logging
import os

def setup_logging(log_file="app.log"):
    """
    Set up logging configuration.
    
    Args:
    log_file (str): Path to the log file.
    """
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def log_info(message):
    """
    Log an info message.
    
    Args:
    message (str): The message to log.
    """
    logging.info(message)

def log_error(message):
    """
    Log an error message.
    
    Args:
    message (str): The message to log.
    """
    logging.error(message)
