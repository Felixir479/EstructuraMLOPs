# process_data.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def process_data(data):
    '''
    Function to process the input data: handles missing values, encoding, and scaling.
    
    Args:
    data (pd.DataFrame): Raw data to be processed.
    
    Returns:
    X_train, X_test, y_train, y_test: Processed and split data ready for model training.
    '''
    # Separate target from predictors
    y = data['target']  # Assumes 'target' is the column name for the target variable
    X = data.drop(columns=['target'])
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Identify categorical and numerical columns
    categorical_cols = [col for col in X.columns if X[col].dtype == 'object']
    numerical_cols = [col for col in X.columns if X[col].dtype in ['int64', 'float64']]
    
    # Define the preprocessing for numeric features
    numeric_transformer = Pipeline(steps=[
        ('scaler', StandardScaler())
    ])
    
    # Define the preprocessing for categorical features
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])
    
    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ])
    
    # Apply preprocessing
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)
    
    return X_train, X_test, y_train, y_test
