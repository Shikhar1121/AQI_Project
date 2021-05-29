# -*- coding: utf-8 -*-


#importing important libraries
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


#linear regression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)

#score = r^2
lr.score(x_train,y_train)


#cross val score
from sklearn.model_selection import cross_val_score
score = cross_val_score(lr,x,y,cv=5)


score.mean()

#prediction
prediction = lr.predict(x_test)

sns.distplot(y_test-prediction)


#Pickle for deployment
import pickle
file = open('regression_model.pkl','wb')

#dump info to that file
pickle.dump(lr,file)
