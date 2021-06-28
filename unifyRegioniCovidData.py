# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 22:15:07 2021

@author: olife
"""

import pandas as pd
import requests
import time
from datetime import date, timedelta

myPath=".."
yesterday = (date.today() - timedelta(days=1)).strftime('%Y%m%d')
t=time.strptime('20200224','%Y%m%d')
newdate=date(t.tm_year,t.tm_mon,t.tm_mday)
tempo=newdate.strftime('%Y%m%d')
url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-20200224.csv" 
download = requests.get(url).content    
frame = pd.read_csv(url,index_col=0,parse_dates=[0],sep=',')

try:
    while tempo!= yesterday :
        print("donwloading "+tempo)
        # Calculating next day
        t=time.strptime(tempo,'%Y%m%d')
        newdate=date(t.tm_year,t.tm_mon,t.tm_mday)+timedelta(1)
        tempo=newdate.strftime('%Y%m%d')
        
        # Downloading the csv file from your GitHub account
        url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-"+tempo+".csv" 
    
        frame2 = pd.read_csv(url,index_col=0,parse_dates=[0],sep=',')
        frame = frame.append(frame2)
    frame.fillna(0,inplace=True)
except:
    print("exception")


frame.to_csv(myPath + "\covid19ItaliaRegioni.csv", sep=';')
