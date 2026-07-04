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

#data_path='sales.xlsx'
#data_name='jan_sales'

def data_clean_master(data_path,data_name):
    print("thank you for giving the details")
    
    sec=random.randint(1,4) #generating random number
    
    #printing delaying message
    print(f'Please wait for {sec}seconds! Checking file path')
    time.sleep(sec)

    #Checking if the path exists
    if not os.path.exists(data_path):
            print("Wrong File Path! Try again")
            return
    else:
        #Checking the file type
        if data_path.endswith('.csv'):
            print('Dataset is csv !')
            data=pd.read_csv(data_path,encoding_errors='ignore')
    
        elif data_path.endswith('.xlsx'):
            print('Dataset is excel file !')
            data=pd.read_excel(data_path)
    
        else:
            print('Unkown File Type !')
            return


    #Showing number of records
    print(f"Dataset contains tatal rows: {data.shape[0]}\n total colmn:{data.shape[1]}")

    #start cleaning

    #checking duplicate
    duplicates=data.duplicated()
    total_duplicate=data.duplicated().sum()

    print(f"Dataset has total duplicates record:{total_duplicate}")

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
    print(f"Dataset contains missing value by column \n {missing_vales_columns}")


#Dealing with misssing values 
#fillna--int and float
#Dropna--any object


    columns=df.columns

    for col in columns:
        if df[col].dtype in (float,int):
            df[col]=df[col].fillna(df[col].mean())
    else:
    #droping all rows with missing records for non number col
        df.dropna(subset=col,inplace=True)

#data is clean now
    print(f"Congratulation! \n Your Dataset is clean now. \n Number of rows :{df.shape[0]}\n Number of columns:{df.shape[1]}")

#saving clean data
    df.to_csv(f'{data_name}clean_data.csv ',index=None)
    print(' Your Dataset is Saved.')


if __name__ == "__main__":
    
    print("Welcome to Data Cleaning Master!")
    # ask path and file name
    data_path = input("Please enter dataset path :")
    data_name = input("Please enter dataset name :")
    
    # calling the function
    data_clean_master(data_path, data_name)
