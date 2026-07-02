# importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random
print(os.getcwd())
print("All modules imported successfully!")
print(os.listdir())

data_path=''
data_name=''

#Checking if the path exists
if not os.path.exists(data_path):
    print("Please enter right path !")
    #return
else:
    #Checking the file type
    if data_path.endswith('.csv'):
        print('Dataset is csv !')
        data=pd.read_csv(data_path,encoding_errors='ignore')
    
    elif data_path.endswith('.xlsx'):
        print('Dataset is excel file !')
        data=pd.read_excel(data_path,encoding_errors='ignore')
    
    else:
        print('Unkown File Type !')
        #return


#Showing number of records
print(f"Dataset contains tatal rows: {data.shape[0]}\n total colmn:{data.shape[1]}")

#start cleaning

#checking duplicate
duplicates=data.duplicated()
total_duplicate=data.duplicated().sum()

print(f"Dtataset has total duplicates record:{total_duplicate}")

#Saving duplicates
if total_duplicate>0:
    duplicate_records=data[duplicates]
    duplicate_records.to_csv(f'{data_name}duplicate.csv', index=None)

#Deleting duplicate
df=data.drop_duplicates()

#Finding missing values
total_missing_vales=df.isnull().sum().sum()
missing_vales_columns=df.isnull().sum()

print(f'Dataset has total mising value:{total_missing_vales}')
print(f"Dtataset contains missing value by column \n {missing_vales_columns}")


#Dealing with misssing values 
#fillna--int and float
#Dropna--any object



