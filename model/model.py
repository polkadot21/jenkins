import pandas as pd
import statsmodels.api as sm
import plotly.express as px
import plotly.graph_objs as go
from joblib import dump, load
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


from  urllib.request import urlretrieve
#download data
url = 'https://archive.org/download/ages-and-heights/AgesAndHeights.pkl'
urlretrieve(url,"AgesAndHeights.pkl" )
#upload data in pandas
data = pd.read_pickle("AgesAndHeights.pkl")

#get rid of the negative ages
data = data[data['Age'] > 0]

#inches to cm
data["Height"] = data["Height"].apply(lambda x: x*2.54)

#train/test
train, test = train_test_split(data, test_size=0.2)

#define the predictor and exogeneuous variables
X_train = sm.add_constant(train['Age'])
Y_train = train["Height"]
X_test = sm.add_constant(test['Age'])
Y_test = test["Height"]

#define and fit the model
model = sm.OLS(Y_train, X_train)
results = model.fit()

#make predictions
predictions = results.predict(X_test)

#save model
dump(model, 'model.joblib')

