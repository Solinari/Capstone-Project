# for pandas
import pandas as pd

# Open method, query demonstration

def OpenCSV2DF(file):
    '''opens a csv file
       returns it as a dataframe'''
    df = pd.read_csv(file)

    return df


# structure is:
# Dataframe[Dataframe[column] == condition]
# casting this as a string returns it as a string
# normally it is a dataframe object

def testQueryPrint(df, myClass, mySeason):
    ''' Test querying from class and season'''
    
    print(df[(df['Class Name'] == myClass) & (df['Season'] == mySeason)])


# test open
myDF = OpenCSV2DF('Catalog.csv')

testQueryPrint(myDF, 'CSC 421', 'Spring 2011-2012')


