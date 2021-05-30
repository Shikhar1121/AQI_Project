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


from sklearn.tree import DecisionTreeRegressor

dtree = DecisionTreeRegressor(criterion='mse')

dtree.fit(x_train, y_train)

print(dtree.score(x_train, y_train))

print(dtree.score(x_test,y_test)) 

#test score reveal that this is a case of overfitting so we need to do hyperparameter tuning
#Hyperparameter tuning
DecisionTreeRegressor()


#Setting various parameters
params ={ 
    'splitter':['best','random'],
    'max_depth':[3,4,5,6,7,8,9,10],
    'min_samples_leaf':[1,2,3,4,5],
    'min_weight_fraction_leaf':[0.1,0.2,0.3,0.4,0.5],
    'max_features':[ "auto","sqrt", "log2",None],
    'max_leaf_nodes' : [None,10,20,30,40,50]
        }


#Import gridsearchcv
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(dtree,params,scoring = 'neg_mean_squared_error',n_jobs=1,cv = 10,verbose=3)

# =============================================================================
# #function for knowing thw time it takes to create this model
# def timer(start_time = None):
#     if not start_time:
#         start_time= datetime.now()
#         return start_time
#     elif start_time:
#         thour,temp_sec = divmod((datetime.now()-start_time).total_seconds(),3600)
#         tmin,tsec = divmod(temp_sec,60)
#         
# =============================================================================

grid_search.fit(x,y)

grid_search.best_params_
grid_search.best_score_


predictions = grid_search.predict(x_test)

from sklearn import metrics
print('MAE : {}'.format(metrics.mean_absolute_error(y_test,predictions)))
print('MSE : {}'.format(metrics.mean_squared_error(y_test,predictions)))
print('RMSE : {}'.format(np.sqrt(metrics.mean_absolute_error(y_test,predictions))))


import pickle
file = open('decision_tree_regressor.pkl','wb')

#dump info to that file
pickle.dump(grid_search,file)





#Tree Visualisation
# =============================================================================
# from IPython.display import Image
# from sklearn.externals.six import StringIO
# from sklearn.tree import export_graphviz
# import pydotplus
# 
# 
# features = list(df.columns[:-1]) #converting independent columns as list as graphviz takes them as a list
# features
# 
# 
# import os
# =============================================================================



