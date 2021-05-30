# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv('Data/Real Data/Real_Combine.csv')

##check for null values
df.isnull().sum()


#only missing value is in PM2.5,since only one null value we can drop it
df = df.dropna()


#division into dependent and independent features
x= df.iloc[:,:-1]#independent features
y = df.iloc[:,-1]#dependent features


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor()
rfr.fit(x,y)

rfr.score(x_train,y_train)

rfr.score(x_test,y_test)

#HyperParameter Tuning

RandomForestRegressor()
from sklearn.model_selection import RandomizedSearchCV

n_estimators= [int(x) for x in np.linspace(start=100, stop=1200, num=10)]
max_features = ['auto','sqrt','log2',None]
max_depth = [int(x) for x in np.linspace(5,30,6)]
min_samples_split = [2,5,10,20,15,25]
min_samples_lea = [1,2,3,4,5,10]

params = {
    'n_estimators':n_estimators,
    'max_features':max_features,
    'max_depth':max_depth,
    'min_samples_split':min_samples_split,
    'min_samples_leaf':min_samples_lea 
    }

rfr2 = RandomForestRegressor()

rf_random = RandomizedSearchCV(rfr2,params,scoring='neg_mean_squared_error',n_iter=100,cv=5,verbose=2,random_state=42)

rf_random.fit(x_train,y_train)


rf_random.best_params_    
rf_random.best_score_

predictions = rf_random.predict(x_test)

from sklearn import metrics
print('MAE : {}'.format(metrics.mean_absolute_error(y_test,predictions)))
print('MSE : {}'.format(metrics.mean_squared_error(y_test,predictions)))
print('RMSE : {}'.format(np.sqrt(metrics.mean_absolute_error(y_test,predictions))))


