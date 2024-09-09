# load_data.py

import pandas as pd
from sqlalchemy import create_engine

def get_sql_connection(connection_string):
    '''
    Establish a connection to the database using SQLAlchemy.
    
    Args:
    connection_string (str): Database connection string.
    
    Returns:
    connection: Database connection object.
    '''
    engine = create_engine(connection_string)  # Create the engine
    connection = engine.connect()  # Open the connection
    return connection

def load_data_from_sql(connection, query):
    '''
    Load data from an SQL database using a query.
    
    Args:
    connection: Database connection object.
    query (str): SQL query to extract data.
    
    Returns:
    DataFrame: Loaded data as a pandas DataFrame.
    '''
    data = pd.read_sql(query, connection)  # Execute the SQL query and load data into a DataFrame
    connection.close()  # Close the connection after loading the data
    return data
