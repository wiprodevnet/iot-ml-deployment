"""
Linear Regression model data preperation and storage as pickle model
"""
import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Linear Regression Model implementation
def train_test_rmse(feature_cols):
    """ Define a function that accepts a list of features and returns model and RMSE """
    # create X and y
    x_input = ENERGY[feature_cols]
    y_output = ENERGY.Global_active_power
    x_train, x_test, y_train, y_test = train_test_split(x_input, y_output, random_state=123)
    linreg = LinearRegression()
    linreg.fit(x_train, y_train)
    y_pred = linreg.predict(x_test)

    return (linreg, np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# IOT dataset downloaded from https://data.world/databeats/household-power-consumption

# Read the csv file to pandas dataframe & clean the data
# As there are some na values with ? mark these as na values
ENERGY = pd.read_csv('household_power_consumption.csv', na_values='?')

# Drop null values
ENERGY.dropna(inplace=True)

# Add the 'datetime' as the index cloumn and derive a new 'hour' column
ENERGY['datetime'] = pd.to_datetime(ENERGY['Date']+' '+ ENERGY['Time'])
# Set datetime name as index column
ENERGY.set_index("datetime", inplace=True)
# Remove old date time columns
ENERGY = ENERGY.drop(['Date', 'Time'], axis=1)
# Derive time of the day (hour) to add this as a feature for linear regression
ENERGY['hour'] = ENERGY.index.hour

# Create dummy variables based on hour
HOUR_DUMMIES = pd.get_dummies(ENERGY.hour, prefix='hour')

# Drop redundant categorical column - hour_0
# Note for N categories, it is enough to have N-1 as features
HOUR_DUMMIES.drop(HOUR_DUMMIES.columns[0], axis=1, inplace=True)

# Concatenate the original DataFrame and the dummy DataFrame
ENERGY = pd.concat([ENERGY, HOUR_DUMMIES], axis=1)

# Model #1 Simple model
print('Model #1 Simple univariant model ')
# Train and test the liner regression model using 'hour' as feature
# and active power as output
(MODEL, ERROR) = train_test_rmse(['hour'])
INPUT = np.array([[0]])

# Print the mse error on the test data
print('MSE', ERROR)
# Predict the out output for given input
PREDICTION = MODEL.predict(INPUT)
# Print the linear MODEL cofficients and output
print('intercept_', MODEL.intercept_)
print('coef_', MODEL.coef_)
print('Predicted', PREDICTION)

#Store the model as a pkl for deployment
FILE = open('iotmodel.pkl', 'wb')
pickle.dump(MODEL, FILE)
FILE.close()

# Model #2 Higher polynomial model with categorical columns
print('Model #2  Multiple categories model ')
FEATURE_COL = ENERGY.columns[ENERGY.columns.str.startswith('hour_')]
print(FEATURE_COL)

# Let us train and test the liner regression model using all categorical cloumns 'hour_' as feature
# and active power as output
(MODEL, ERROR) = train_test_rmse(FEATURE_COL)

INPUT = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]])

# Print the mse error on the test data
print('MSE', ERROR)
# Predict the out output for given input
PREDICTION = MODEL.predict(INPUT)
# Print the linear MODEL cofficients and output
print('intercept_', MODEL.intercept_)
print('coef_', MODEL.coef_)
print('Predicted', PREDICTION)

# Store the second model as a pkl for deployment
FILE = open('iotmodel2.pkl', 'wb')
pickle.dump(MODEL, FILE)
FILE.close()
