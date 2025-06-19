from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import pandas as pd

def train_model(df, target_col):
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Encode categorical if any
    X = pd.get_dummies(X, drop_first=True)
    if y.dtype == 'object':
        y, class_names = pd.factorize(y)
    else:
        class_names = None

    # Align columns in case encoding caused issues
    X = X.loc[:, ~X.columns.duplicated()]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model selection
    is_classification = class_names is not None
    model = RandomForestClassifier() if is_classification else RandomForestRegressor()

    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    from math import sqrt
    score = sqrt(mean_squared_error(y_test, y_pred))  # manually calculate RMSE

    return model, X_test, y_test, y_pred, score, is_classification, class_names
