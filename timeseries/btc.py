import datetime
#Libraries to manipulate data
import numpy as np
import math
import pandas as pd
#Libraries to visualize data
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dense, LSTM, Dropout, GRU, Bidirectional
from tensorflow.keras.optimizers import SGD
from keras.layers import LSTM

import os
import warnings
warnings.filterwarnings(action='ignore')
warnings.filterwarnings(action='ignore', category=DeprecationWarning)
warnings.filterwarnings(action='ignore', category=FutureWarning)


path = "BTC2.xlsx"
#while executing at your side, please add path to the same dataset on your machine.


df = pd.read_excel(path)
df['date'] = df['Tarih']
df['price'] = df['Açılış']
df = df.drop(columns = ['Tarih', 'Açılış'])
df['price'].fillna(method='ffill', inplace=True)


split = len(df) - int(len(df) * 0.8)
df_train = df.iloc[split:]
df_test = df.iloc[:split]

step = 21


def prepeare_data(df, step):
    data = []

    for i in range(len(df) - step):
        data.append((df[i: (i + step)]).values)

    return np.array(data)

X_train = prepeare_data(df_train.price, step)
X_test = prepeare_data(df_test.price, step)

print("X_train shape= ", X_train.shape)
print("X_test shape= ", X_test.shape)


y_train = df_train.price[step:].values
y_test = df_test.price[step:].values

print("y_train shape= ", y_train.shape)
print("y_test shape= ", y_test.shape)



model = Sequential()
model.add(LSTM(units=128, activation='relu', dropout=0.2, input_shape=(21,1))) # Input layer
model.add(Dense(units=1)) # Output layer
model.compile(optimizer='adam', loss='mae') #rmse?
model.fit(X_train, y_train, epochs=30, batch_size=7)

model.save('btc_model')

preds = model.predict(X_test)
mean_absolute_error(preds, y_test)

def return_rmse(test,predicted):
    rmse = math.sqrt(mean_squared_error(test, predicted))
    print("The root mean squared error is {}.".format(rmse))
return_rmse(y_test, preds)

def plot_predictions(test,predicted):
    fig, ax = plt.subplots(1, figsize=(16, 9))
    plt.plot(test, color='red',label='Real Price')
    plt.plot(predicted, color='blue',label='Predicted Price')
    plt.title('Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
plot_predictions(y_test,preds)