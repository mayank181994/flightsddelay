#!/usr/bin/env python
import numpy as np 
import pandas as pd

df1=pd.read_csv("flightdelays.csv")
print(df1[df1["Cancelled"]==0]['Dest'].value_counts().head(3))

Echo"My name is Mayank"
