# getting all necessary imports
import pandas as pd


# loading the dataset into a pandas dataframe
finDF = pd.read_csv('credit_risk_dataset.csv')


# print(finDF['loan_status'])

# checking if there is any value in loan_status column that is not 0 or 1
# since 0 is non default and 1 is default
for status in finDF['loan_status']:
    if not status == 0 and not status == 1:
        print(status)

##### Cleaning up dataset #####

# 1. Dropping all empty cells
finDF.dropna(inplace=True)

# 2. 