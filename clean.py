import pandas as pd
import numpy as np
import re

data = pd.read_csv('file.csv')
nullData = data.isnull().sum() #there are some articles which don't have a summary / paragraph
duplicated = data.duplicated()

for k in range(len(duplicated)):
   if duplicated[k] == True:
    print(data['id'][k], " / ", data['theme'][k], " / ", data['title'][k]) #prints part of the content of the duplicated line

#data['date'] = pd.to_datetime(data['date'], format='% %th %' or '% %st %' or '% %nd %' or '% %rd %', errors='coerce') to change the dates to a certain format
    

