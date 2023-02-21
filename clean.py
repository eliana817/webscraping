import pandas as pd
import numpy as np
import re

data = pd.read_csv('file.csv')

###################### Check and delete duplicated lines ######################## 

duplicated = data.duplicated()

for k in range(len(duplicated)):
   if duplicated[k] == True:
    print(data['id'][k], " / ", data['theme'][k], " / ", data['title'][k]) #prints part of the content of the duplicated line

data.drop_duplicates(subset=None, inplace=True) #subset = None means that we take into account every column when checking for duplicates
                                                #and not specific ones. inplace = True means that we remove the duplicate lines if there are any

data.to_csv('file.csv', index=False) #apply the changes to the main file

######################## Make sure that the dates are in the correct format #######################

#data['date'] = pd.to_datetime(data['date'], format='% %th %' or '% %st %' or '% %nd %' or '% %rd %', errors='coerce') to change the dates to a certain format

######################## Check for empty data and replace it with another value ######################

print("Number of articles with no summary: ",data['summary'].isnull().sum()) #counts number of lines with no summary

data['summary'] = data['summary'].fillna("No summary") #replace the empty data with No summary data

data.to_csv('file.csv',index=False) #replace the original data with the new modified one: mdata

#OR 

#mdata = data.fillna('No summary') This will replace all empty data, not only in the summary column
#mdata.to_csv('file.csv', index=False)

#print(mdata['summary'].isnull().sum()) check that there are no more empty summaries any more 

######################## Change the date column type ########################

data['date'] = pd.to_datetime(data['date']) #change the date column type from object to date
