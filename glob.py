import glob
import pandas as pd
import os 

folder_name = 'D:\\SafeExpress26thAug'
file_type = 'csv'
seperator = ','
dataframe = pd.concat([pd.read_csv(f,sep=seperator) for f in glob.glob(folder_name + "/*."+file_type)],ignore_index=True)

def new_func(dataframe):
    print(dataframe.head(3))
    
new_func()
