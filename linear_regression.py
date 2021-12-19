import numpy as np
from sklearn.linear_model import LinearRegression
import joblib


x_train = np.random.randn(30, 2) * 1.5
y_train = np.random.randn(30)+ 2 * x_train[:, 0] - 0.5 * x_train[:, 1]

model = LinearRegression()
model.fit(x_train, y_train)

joblib.dump(model, 'linear_regression.joblib')