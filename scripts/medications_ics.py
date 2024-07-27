import sqlite3
import pandas as pd

# Connect to the sqlite3 database. Read the medications table as a dataframe
medications_df = pd.read_csv('../original-data/medications.csv')
medications_df = medications_df.fillna('')


# IC: Drugs with more than 1 drug in the name
icv_multiple_drugs = medications_df[medications_df['RXDDRUG'].str.contains(';', na=False)]
print(f'Number of rows with multiple drugs in 1 column: {icv_multiple_drugs.shape[0]}')


# IC: Empty drug name
icv_empty_drug_name = medications_df[medications_df['RXDDRUG'].str.strip() == '']
print(f'Number of rows with empty drug name: {icv_empty_drug_name.shape[0]}')

# IC: Numeric drug name
icv_numeric_drug_name = medications_df[medications_df['RXDDRUG'].str.isnumeric()]
print(f'Number of rows with numeric drug name: {icv_numeric_drug_name.shape[0]}')
