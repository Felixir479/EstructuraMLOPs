
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Class to manage project configuration parameters.
    """
    def __init__(self, db_choice="postgresql"):
        # Dictionary of database connection strings
        self.databases = {
            "postgresql": {
                "connection_string": f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
            },
            "mysql": {
                "connection_string": f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
            },
            "sqlite": {
                "connection_string": "sqlite:///path_to_your_database.db"
            },
            "mssql": {
                "connection_string": f"mssql+pyodbc://{os.getenv('MSSQL_USER')}:{os.getenv('MSSQL_PASSWORD')}@{os.getenv('MSSQL_HOST')}/{os.getenv('MSSQL_DB')}?driver=ODBC+Driver+17+for+SQL+Server"
            },
            "oracle": {
                "connection_string": f"oracle+cx_oracle://{os.getenv('ORACLE_USER')}:{os.getenv('ORACLE_PASSWORD')}@{os.getenv('ORACLE_HOST')}:{os.getenv('ORACLE_PORT')}/{os.getenv('ORACLE_SID')}"
            },
            "mongodb": {
                "connection_string": f"mongodb://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASSWORD')}@{os.getenv('MONGO_HOST')}/{os.getenv('MONGO_DB')}"
            },
            "redshift": {
                "connection_string": f"redshift+psycopg2://{os.getenv('REDSHIFT_USER')}:{os.getenv('REDSHIFT_PASSWORD')}@{os.getenv('REDSHIFT_HOST')}:{os.getenv('REDSHIFT_PORT')}/{os.getenv('REDSHIFT_DB')}"
            },
            "cassandra": {
                "connection_string": f"cassandra://{os.getenv('CASSANDRA_HOST')}/{os.getenv('CASSANDRA_KEYSPACE')}"
            }
        }
        
        # Choose the database connection string
        self.db_connection_string = self.databases[db_choice]["connection_string"]
        
        # SQL query to retrieve the data
        self.query = os.getenv("QUERY", "SELECT * FROM transactions")
        
        # Model parameters
        self.model_params = {
            "n_estimators": 100,  # Number of trees in the forest
            "max_depth": 10,  # Maximum depth of the trees
            "random_state": 42  # Seed for reproducibility
        }
        
        # Path to deploy the trained model
        self.deploy_path = os.getenv("DEPLOY_PATH", "models/deployed_model.pkl")
