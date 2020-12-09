import pandas as pd
import csv
import urllib.request
from urllib.parse import urlparse
from urllib import response
import re

class DataClass:
        def __init__(self, state=None,country=None):
                self.state = state
                self.country=country

        url = 'https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv' #the url we get the raw data from
        response = urllib.request.urlopen(url) #requesting the url
        data = pd.read_csv(response,sep=',')  #reading the url.
        #print(data.head(0)) #prints the head of the file.
       # print(data[['Country/Region']])
        data = data.drop('Lat',axis=1) #deletes column named : Lat
        data = data.drop('Long',axis=1) #deletes column named : Long
        data=data.groupby('Country/Region')
        col = ['Province/State','Country/Region']
        datalist = [] #a list which we want to save our data in
        #for col in data:
       
        for rows in data.itertuples():
                obj = DataClass(data.loc[1], data.loc[2])
        #data.get_group('Country/Region')
        mylist=data[col[1]]
        
        datalist.append(mylist)#saves the states&countries in a list.
        
        
        print(datalist)

                #merge the countries.
               

#.decode('utf-8').split('\n')

#data[data["Area"] == "Ireland"] //auto gia ta polla states.
   
  
