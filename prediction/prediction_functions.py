import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.metrics import make_scorer, mean_squared_error, r2_score, mean_absolute_error, explained_variance_score

# Custom RMSE scorer
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

# Custom calibration slope scorer
def calibration_slope(y_true, y_pred):
    model = ElasticNet()
    model.fit(y_pred.reshape(-1, 1), y_true)
    return model.coef_[0]

# Custom calibration intercept scorer
def calibration_intercept(y_true, y_pred):
    model = ElasticNet()
    model.fit(y_pred.reshape(-1, 1), y_true)
    return model.intercept_

# Define the scorers dictionary
scorers = {
    'rmse': make_scorer(rmse), # NC:I removed greater_is_better=False, this only needs setting if using scorer in a loss function 
    'r2': make_scorer(r2_score),
    'mae': make_scorer(mean_absolute_error),
    'explained_variance': make_scorer(explained_variance_score),
    'calibration_slope': make_scorer(calibration_slope),
    'calibration_intercept': make_scorer(calibration_intercept)
}