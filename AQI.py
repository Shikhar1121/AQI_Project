# -*- coding: utf-8 -*-
"""
Created on Mon May 24 23:17:29 2021

@author: Shikhar
"""
import time #To find execution time
import requests #to download html page in the form of requests.
import os
import sys


def retrieve_html():
    for year in range(2013,2019): #for years in range 2013 to 2018
        for month in range(1,13):
            if (month<10):
               url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month,year) #for month less than 10
            else:
                 url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year) #for month greater than than 10
            request_texts = requests.get(url)
            text_utf = request_texts.text.encode('utf=8')
        
            if not os.path.exists("Data/Html_Data/{}".format(year)): #checks if folder with the name of the year is present inside the data folder or not if not it get inside the if
                os.makedirs("Data/Html_Data/{}".format(year)) #it gets inside if and makes a folder.
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output: #helps in opening folders
                output.write(text_utf)
            
        sys.stdout.flush()

if __name__ =="__main__":
   start_time = time.time()
   retrieve_html()
   stop_time = time.time()
   print("Time Taken = {}".format(stop_time-start_time))