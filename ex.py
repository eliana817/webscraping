import pandas as pd
import numpy as np
import re
import csv 

data = pd.read_csv('operations.csv')

headerList = list(data) #makes a list out of the headers
lines = len(data.index) #number of lines in the csv file

######################## Step 1 - check for empty lines and fill them with another value ########################

for h in headerList:
    if data[h].isnull().sum() > 0:
        if h == 'categ':
            data['categ'] = data['categ'].fillna('AUTRE') #replace the empty lines in the categ column with "AUTRE" 
        elif h == 'montant':
            mdata = data.loc[data['montant'].isnull(),:]
            for n in mdata.index:
                data['montant'][n] = data['solde_avt_ope'][n+1] - data['solde_avt_ope'][n]

data.to_csv('operations.csv')

######################## Step 2 - check for duplicates and remove if necessary ########################

data.drop_duplicates(subset=None, inplace=True) #subset = None means that we take into account every column when checking for duplicates
                                                #and not specific ones. inplace = True means that we remove the duplicate lines if there are any

data.to_csv('operations.csv', index=False) #apply the changes to the main file

######################## Step 3 - check for unlikely values ########################

montantMin = data['montant'].min() #get the min value
montantMax = data['montant'].max() #get the max value

for k in range (lines):
    if data['montant'][k] == montantMin:
        data['montant'][k] = data['solde_avt_ope'][k+1] - data['solde_avt_ope'][k] #calculate the correct value

data.to_csv('operations.csv')

#every time the script is run the montantMin value will change only if it is wrong compared to data['solde_avt_ope'][k+1] - data['solde_avt_ope'][k]
#outputs 'A value is trying to be set on a copy of a slice from a DataFrame' error but still works
