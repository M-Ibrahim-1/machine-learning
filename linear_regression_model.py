import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle
import matplotlib as plt

class SimpleLinearRegression:
    def train():
        dataset = pd.read_csv("dataset.csv")
        dataset['res-force'] = dataset['res-force'].apply(np.ceil)
        dataset.drop(['Unnamed: 0'], axis=1, inplace=True)
        print(dataset)
        x = dataset.iloc[:, :-1].values
        print(x)
        y = dataset.iloc[:, -1].values
        x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                            test_size=0.2,
                                                            random_state=1)
        regressor = LinearRegression()
        regressor.fit(x_train, y_train)
        y_pred = regressor.predict(x_test)
        np.set_printoptions(precision=2)
        print(np.concatenate(
            (y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)),
            1))
        print("**************************")
        print(f"R squared = {r2_score(y_test, y_pred)}")
        filename = "linear_regression_model.sav"
        pickle.dump(regressor, open(filename, 'wb'))
        return regressor
    @staticmethod
    def predict(position, velocity, angle, depth, width):
        regressor = pickle.load(open('Random_forest_model.sav', 'rb'))
        resultant_force = regressor.predict([[position,
                                              velocity,
                                              angle,
                                              depth,
                                              width]])
        return resultant_force

