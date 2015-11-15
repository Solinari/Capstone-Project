# parserDataDump.py

# for pandas
import pandas as pd

def OpenCSV2DF(file):
    '''opens a csv file
       returns it as a dataframe'''
    df = pd.read_csv(file)

    return df

myDF = OpenCSV2DF('Catalog.csv')

# structure is:
# Dataframe[Dataframe[column] == condition]
# casting this as a string returns it as a string
# normally it is a dataframe object
print(myDF[(myDF['Class Name'] == 'CSC 421') & (myDF['Season'] == 'Spring 2011-2012')])
