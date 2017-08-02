# coding=utf-8
#from GreenTaxi.models import request_table
import csv
import pandas as pd
from datetime import datetime

df = pd.read_csv('E:/NYU Docs/Revmax_Project/new.csv')

def transform(i):
    d = datetime.strptime(i, "%d-%m-%Y %H:%M")
    answer = d.strftime("%Y-%m-%d %H:%M")
    return answer

df['start_time'] = df['start_time'].apply(lambda x: transform(x))
df['end_time'] = df['end_time'].apply(lambda x: transform(x))
df.to_csv("finaldata.csv")



