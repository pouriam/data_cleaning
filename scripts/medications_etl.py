import sqlite3
import pandas as pd

# Connect to the sqlite3 database. Read the medications table as a dataframe
conn = sqlite3.connect('../clean-data/clean_data.sqlite')
medications_df = pd.read_sql_query('SELECT * from medications', conn)

# Drop some columns we won't need
medications_df = medications_df.drop(['drug_used', 'drugs_count'], axis=1)

# Combine all the 4 drug columns into a single column, containing a list of drugs
def combine_drug_names(row):
    drugs = []
    if row['drug_name1'] is not None:
        drugs.append(row['drug_name1'].strip())
    if row['drug_name2'] is not None:
        drugs.append(row['drug_name2'].strip())
    if row['drug_name3'] is not None:
        drugs.append(row['drug_name3'].strip())
    if row['drug_name4'] is not None:
        drugs.append(row['drug_name4'].strip())
    return drugs

medications_df['drug_names'] = medications_df.apply(combine_drug_names, axis=1)
medications_df = medications_df.drop(['drug_name1', 'drug_name2', 'drug_name3', 'drug_name4'], axis=1)

# Use pd.explode on that new column, to create a new row for each drug
medications_df = medications_df.explode('drug_names')
medications_df = medications_df.rename(columns={
    'drug_names': 'drug_name'
})

# Write the new dataframe to a csv file
medications_df.to_csv('medications_exploded.csv')