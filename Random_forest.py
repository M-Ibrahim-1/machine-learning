#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
#Importing the dataset

#Training the Random Forest Regression model on the whole dataset
#n_estimators = no of Trees

def predict_from_meta_model():
    pos = input("please enter the Postion: ")
    vel = input("please enter the velocity: ")
    angle = input("please enter the angle: ")
    depth = input("please enter the depth: ")
    width = input("please enter the width: ")
    resultant_force = regressor.predict([[pos, vel, angle, depth, width]])
    return resultant_force


def import_dataset():
    dataset = pd.read_csv("dataset.csv")
    dataset['res-force'] = dataset['res-force'].apply(np.ceil)
    dataset.drop(['Unnamed: 0'], axis=1, inplace=True)

    print(dataset)
    x = dataset.iloc[:, :-1].values
    print(x)
    y = dataset.iloc[:, -1].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                        random_state=1)
    return x_train, x_test, y_train, y_test


regressor = RandomForestRegressor(n_estimators=500, random_state=1)
x_train, x_test, y_train, y_test = import_dataset()

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

#Evaluating the Model Performance
print("************")
print(r2_score(y_test, y_pred))
