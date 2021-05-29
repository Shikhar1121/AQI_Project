# -*- coding: utf-8 -*-
#extract(webscrap) data from html files using beautifulsoup and combime it with AQI data

from plot_AQI import avg_2013,avg_2014,avg_2015,avg_2016

import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup #helps in html webscrapping
import os
import csv






def met_data(month,year): 
    #to webscrap files from each and every html file
    
    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month),'rb') #opening whole html file in read byte form
    plain_file = file_html.read() #as soon as we open a file using beautiful soup we have to read it immediately
    
    
    tempD = []
    finalD = []  #final list of parameters
    
    
    soup = BeautifulSoup(plain_file,"lxml") #lxml is a format for beautiful soup
    
    for table in soup.findAll('table',{'class':'medias mensuales numspan'}): #for extraction data from table in html file with class "medias
        for tbody in table:#to oterate the  table body & tbody is list of table rows
            for tr in tbody: #for iterating through each row in tbody
                a = tr.get_text() #text from each row
                tempD.append(a) #appending the extracted text into tempD
    
    
    rows = len(tempD)/15 #to get the rows divide the len of the list with the no of columns since it is rows*columns
    
    for times in range(round(rows)): #iterating through each and every row
        newtempD =[]
        
        for i in range(0,15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
        
    length = len(finalD)
    
    finalD.pop(length-1) #for droppinh monthly means useless column
    finalD.pop(0) #features column
    
    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)
        
    return finalD

def data_combine(year, cs):
    for a in pd.read_csv('Data/Real Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == '__main__':
    if not os.path.exists('Data/Real Data'):
        os.makedirs('Data/Real Data')
    
    for year in range(2013,2017):
        final_data =[]
        with open('Data/Real Data/real_{}.csv'.format(year),'w') as csvfile:
            wr = csv.writer(csvfile,dialect='excel')
            wr.writerow(['T','TM','Tm','SLP','H','W','V','VM','PM 2.5'])
            
        for month in range(1,13):
            temp =met_data(month,year)
            final_data = final_data+ temp
            
        pm = getattr(sys.modules[__name__],'avg_{}'.format(year))()
        
        if len(pm) ==364:
            pm.insert(364,'_')
        
        for i in range(len(final_data)-1):
            final_data[i].insert(8,pm[i])
        
        

        with open('Data/Real Data/real_{}.csv'.format(year),'a') as csvfile:
             wr = csv.writer(csvfile,dialect='excel')
             for row in final_data:
                flag = 0
                for elem in row:
                    if elem == '' or elem == '-':
                        flag =1
                if flag!=1:
                    wr.writerow(row)

                    
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
     
    total=data_2013+data_2014+data_2015+data_2016
    
    with open('Data/Real Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
df = pd.read_csv('Data/Real Data/Real_Combine.csv')
        
    
    