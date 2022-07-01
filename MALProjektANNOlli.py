#Importing necessary Libraries
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
import sklearn.preprocessing
from sklearn.model_selection import train_test_split
import sklearn.utils
import sklearn.metrics as sm
import pickle
import dill
import weakref

#Loading Dataset
data = pd.read_csv("dataset.csv")
#Drop first Row (irrelevent Data)
data.drop('Unnamed: 0', inplace=True, axis=1)
#Shuffling Data
data = shuffle(data)
print(data)
#Generating Matrix of Features (X) and Dependent Variable Vectors (Y)
X = data.iloc[:,1:-1].values
Y = data.iloc[:,-1].values

#Splitting dataset into training and testing dataset
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

#Performing Feature Scaling
Y_train = Y_train.reshape(-1, 1)
Y_test = Y_test.reshape(-1, 1)
X_scaler = sklearn.preprocessing.MinMaxScaler()
Y_scaler = sklearn.preprocessing.MinMaxScaler()
X_scaler.fit(X_train)
Y_scaler.fit(Y_train)
Y_train = Y_scaler.transform(Y_train)
Y_test = Y_scaler.transform(Y_test)
X_train = X_scaler.transform(X_train)
X_test = X_scaler.transform(X_test)

#Initialising ANN
ann = tf.keras.models.Sequential()

#Adding Layers
#Adding Input Layer
ann.add(tf.keras.layers.Dense(units=5,activation="relu"))
#Adding Hidden Layers
ann.add(tf.keras.layers.Dense(units=20,activation="relu"))
ann.add(tf.keras.layers.Dense(units=20,activation="relu"))
ann.add(tf.keras.layers.Dense(units=20,activation="relu"))
#Adding Output Layer
ann.add(tf.keras.layers.Dense(units=1, activation="linear"))

#Compiling ANN
ann.compile(optimizer="adam", loss="mean_squared_error")

#Fitting ANN
ann.fit(X_train, Y_train, batch_size=32, epochs=100)

#Saving created neural network
# serialize model to JSON
model_json = ann.to_json()
with open("ann_model1.json", "w") as json_file:
    json_file.write(model_json)
#serialize weights to HDF5
ann.save_weights("ann_model1.h5")
print("Saved model to disk")
#Evaluating Model
Y_pred = ann.predict(X_test)
Y_test = Y_scaler.inverse_transform(Y_test)
Y_pred = Y_scaler.inverse_transform(Y_pred)

def eval_model():
    print(data)
    res = "\n".join("{} {}".format(X, Y) for X, Y in zip(Y_test, Y_pred))
    print(res)
    print("Mean absolute error =", round(sm.mean_absolute_error(Y_test, Y_pred), 2))
    print("Mean squared error =", round(sm.mean_squared_error(Y_test, Y_pred), 2))
    print("Median absolute error =", round(sm.median_absolute_error(Y_test, Y_pred), 2))
    print("Explain variance score =", round(sm.explained_variance_score(Y_test, Y_pred), 2))
    print("R2 score =", round(sm.r2_score(Y_test, Y_pred), 2))
    return

eval_model()