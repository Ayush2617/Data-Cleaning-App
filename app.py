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
print(f"Dataset contains tatal rows: {}\n total colmn:{}")
