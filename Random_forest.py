#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

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
    return x, y


regressor = RandomForestRegressor(n_estimators=500, random_state=1)
x, y = import_dataset()

regressor.fit(x, y)

print(predict_from_meta_model())





