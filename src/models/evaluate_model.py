# evaluate_model.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def evaluate_model(model, X_test, y_test):
    '''
    Function to evaluate a trained model using several metrics.
    
    Args:
    model: Trained model.
    X_test: Features of the test set.
    y_test: True labels of the test set.
    
    Returns:
    A dictionary with the calculated metrics.
    '''
    # Predict the labels
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1_score': f1_score(y_test, y_pred, average='weighted'),
        'confusion_matrix': confusion_matrix(y_test, y_pred).tolist()  # Convert to list for better serialization
    }
    
    return metrics
