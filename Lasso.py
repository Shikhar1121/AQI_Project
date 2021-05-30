# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



#reading the dataset
df = pd.read_csv('Data/Real Data/Real_Combine.csv')

##check for null values
df.isnull().sum()

#another way to look for null values is heatmaps
sns.heatmap(df.isnull(),yticklabels=False,cbar=True,cmap='viridis')


#only missing value is in PM2.5,since only one null value we can drop it
df = df.dropna()

#division into dependent and independent features
x= df.iloc[:,:-1]#independent features
y = df.iloc[:,-1]#dependent features

y.isnull().sum()

#univariate analysis 1.Using pairplot 2.correlation 3.Heatmap
#1.
sns.pairplot(df)

#2.
df.corr()


#3.
#get correlation of each feature in the dataset
corrmat = df.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
#plot the heatmap
g = sns.heatmap(df[top_corr_features].corr(),annot=True,cmap='RdYlGn')


#Feature selection
from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor()
model.fit(x,y)

print(model.feature_importances_)


#now look at the target  variable
sns.distplot(y)

#it is right skewed

#train test split
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

#Ridge Regression
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

#ridge regression has a parameter called lambda which is why imported gridsearchcv

ridge = Ridge()
parameters = {'alpha':[1e-15,1e-10,1e-8,1e-5,1e-3,1e-1,1,2,3,5,10,20,30,40,50]}#giving alpha list of values
ridge_regressor = GridSearchCV(ridge,parameters,scoring = 'neg_mean_squared_error',cv=5) #initialising gridsearch cv

ridge_regressor.fit(x,y)

print(ridge_regressor.best_params_)
print(ridge_regressor.best_score_)

#Lsso Regression
from sklearn.linear_model import Lasso


#Lasso regression has a parameter called lambda which is why imported gridsearchcv

lasso = Lasso()
parameters = {'alpha':[1e-15,1e-10,1e-8,1e-5,1e-3,1e-1,1,2,3,5,10,20,30,40,50]}#giving alpha list of values
lasso_regressor = GridSearchCV(lasso,parameters,scoring = 'neg_mean_squared_error',cv=5) #initialising gridsearch cv

lasso_regressor.fit(x,y)

print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_)


#model evlution
prediction = lasso_regressor.predict(x_test)
sns.distplot(y_test-prediction)


#metrics
from sklearn import metrics
print('MAE : {}'.format(metrics.mean_absolute_error(y_test,prediction)))
print('MSE : {}'.format(metrics.mean_squared_error(y_test,prediction)))
print('RMSE : {}'.format(np.sqrt(metrics.mean_absolute_error(y_test,prediction))))


#Pickle for deployment
import pickle
file = open('lasso_regression_model.pkl','wb')

#dump info to that file
pickle.dump(lasso_regressor,file)