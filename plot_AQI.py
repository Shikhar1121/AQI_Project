# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#functions to find the daily AQI as AQI's are given in hourly format.

#2013
def avg_2013():
    temp_i = 0
    average =[]
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize=24):#for readiing rows in 2013 dataset. Chunksize is number of rows reafd at a time
        add_var = 0
        avg = 0.0
        data =[]
        df = pd.DataFrame(data = rows)# converting rows into dataframe
        for index,row in df.iterrows():#iterating through all rows in the dataframe
            data.append(row['PM2.5']) #only taking colomn PM2.5
        for i in data:
            if type(i) is float or type(i) is int: #checking it value is not null
                add_var = add_var+i #adding only integer or float values for average
            elif type(i) is str:
                if i!="NoData" and i!='PwrFail' and i!='---' and i!='InVld':#it check if data is "22" or "373" it converts to floats
                    temp = float(i)#conversion to float
                    add_var=add_var+temp
        avg = add_var/24
        temp_i=temp_i+1

        average.append(avg)
    return average
    
    
    
#2014
def avg_2014():
    temp_i = 0
    average =[]
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize=24):#for readiing rows in 2013 dataset. Chunksize is number of rows reafd at a time
        add_var = 0
        avg = 0.0
        data =[]
        df = pd.DataFrame(data = rows)# converting rows into dataframe
        for index,row in df.iterrows():#iterating through all rows in the dataframe
            data.append(row['PM2.5']) #only taking colomn PM2.5
        for i in data:
            if type(i) is float or type(i) is int: #checking it value is not null
                add_var = add_var+i #adding only integer or float values for average
            elif type(i) is str:
                if i!="NoData" and i!='PwrFail' and i!='---' and i!='InVld':#it check if data is "22" or "373" it converts to floats
                    temp = float(i)#conversion to float
                    add_var=add_var+temp
        avg = add_var/24
        temp_i=temp_i+1

        average.append(avg)
    return average

#2015
def avg_2015():
    temp_i = 0
    average =[]
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize=24):#for readiing rows in 2013 dataset. Chunksize is number of rows reafd at a time
        add_var = 0
        avg = 0.0
        data =[]
        df = pd.DataFrame(data = rows)# converting rows into dataframe
        for index,row in df.iterrows():#iterating through all rows in the dataframe
            data.append(row['PM2.5']) #only taking colomn PM2.5
        for i in data:
            if type(i) is float or type(i) is int: #checking it value is not null
                add_var = add_var+i #adding only integer or float values for average
            elif type(i) is str:
                if i!="NoData" and i!='PwrFail' and i!='---' and i!='InVld':#it check if data is "22" or "373" it converts to floats
                    temp = float(i)#conversion to float
                    add_var=add_var+temp
        avg = add_var/24
        temp_i=temp_i+1

        average.append(avg)
    return average
    
    
#2016   
def avg_2016():
    temp_i = 0
    average =[]
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize=24):#for readiing rows in 2013 dataset. Chunksize is number of rows reafd at a time
        add_var = 0
        avg = 0.0
        data =[]
        df = pd.DataFrame(data = rows)# converting rows into dataframe
        for index,row in df.iterrows():#iterating through all rows in the dataframe
            data.append(row['PM2.5']) #only taking colomn PM2.5
        for i in data:
            if type(i) is float or type(i) is int: #checking it value is not null
                add_var = add_var+i #adding only integer or float values for average
            elif type(i) is str:
                if i!="NoData" and i!='PwrFail' and i!='---' and i!='InVld':#it check if data is "22" or "373" it converts to floats
                    temp = float(i)#conversion to float
                    add_var=add_var+temp
        avg = add_var/24
        temp_i=temp_i+1

        average.append(avg)
    return average
    
    
#2017
def avg_2017():
    temp_i = 0
    average =[]
    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize=24):#for readiing rows in 2013 dataset. Chunksize is number of rows reafd at a time
        add_var = 0
        avg = 0.0
        data =[]
        df = pd.DataFrame(data = rows)# converting rows into dataframe
        for index,row in df.iterrows():#iterating through all rows in the dataframe
            data.append(row['PM2.5']) #only taking colomn PM2.5
        for i in data:
            if type(i) is float or type(i) is int: #checking it value is not null
                add_var = add_var+i #adding only integer or float values for average
            elif type(i) is str:
                if i!="NoData" and i!='PwrFail' and i!='---' and i!='InVld':#it check if data is "22" or "373" it converts to floats
                    temp = float(i)#conversion to float
                    add_var=add_var+temp
        avg = add_var/24
        temp_i=temp_i+1

        average.append(avg)
    return average
    
    
#2018    
def avg_2018():
    temp_i = 0
    average =[]
    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize=24):#for readiing rows in 2013 dataset. Chunksize is number of rows reafd at a time
        add_var = 0
        avg = 0.0
        data =[]
        df = pd.DataFrame(data = rows)# converting rows into dataframe
        for index,row in df.iterrows():#iterating through all rows in the dataframe
            data.append(row['PM2.5']) #only taking colomn PM2.5
        for i in data:
            if type(i) is float or type(i) is int: #checking it value is not null
                add_var = add_var+i #adding only integer or float values for average
            elif type(i) is str:
                if i!="NoData" and i!='PwrFail' and i!='---' and i!='InVld':#it check if data is "22" or "373" it converts to floats
                    temp = float(i)#conversion to float
                    add_var=add_var+temp
        avg = add_var/24
        temp_i=temp_i+1

        average.append(avg)
    return average
    
    

if __name__ =='__main__':
    lst2013 = avg_2013()
    lst2014 = avg_2014()
    lst2015 = avg_2015()
    lst2016 = avg_2016()
    lst2017 = avg_2017()
    lst2018 = avg_2018()
    
    plt.plot(range(0,365),lst2013,label = '2013 data')
    plt.plot(range(0,364),lst2014,label = '2014 data')
    plt.plot(range(0,365),lst2015,label = '2015 data')
    plt.plot(range(0,121),lst2016,label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
    