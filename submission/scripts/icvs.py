import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

# Connect to the sqlite3 database. Read the medications table as a dataframe
df = pd.read_csv('../original-data/medications.csv')
df = df.fillna('')

print('--------------')
print('ICVs in original medications table:')
print('--------------')

print(f'Number of rows: {df.shape[0]}')

# IC: Drugs with more than 1 drug in the name
icv_multiple_drugs = df[df['RXDDRUG'].str.contains(';', na=False)]
print(f'Number of rows with multiple drugs in 1 column: {icv_multiple_drugs.shape[0]}')

# IC: Empty drug name
icv_empty_drug_name = df[df['RXDDRUG'].str.strip() == '']
print(f'Number of rows with empty drug name: {icv_empty_drug_name.shape[0]}')

# IC: Numeric drug name
icv_numeric_drug_name = df[df['RXDDRUG'].str.isnumeric()]
print(f'Number of rows with numeric drug name: {icv_numeric_drug_name.shape[0]}')


print('--------------')
print('ICVs in cleaned medications table:')
print('--------------')

df = pd.read_csv('./medications_exploded.csv')
df = df.fillna('')

print(f'Number of rows: {df.shape[0]}')

# IC: Drugs with more than 1 drug in the name
icv_multiple_drugs = df[df['drug_name'].str.contains(';', na=False)]
print(f'Number of rows with multiple drugs in 1 column: {icv_multiple_drugs.shape[0]}')

# IC: Empty drug name
icv_empty_drug_name = df[df['drug_name'].str.strip() == '']
print(f'Number of rows with empty drug name: {icv_empty_drug_name.shape[0]}')

# IC: Numeric drug name
icv_numeric_drug_name = df[df['drug_name'].str.isnumeric()]
print(f'Number of rows with numeric drug name: {icv_numeric_drug_name.shape[0]}')


print('--------------')
print('ICVs in original questionnaire table:')
print('--------------')

df = pd.read_csv('../original-data/questionnaire.csv')
df = df.fillna('')

print(f'Number of rows: {df.shape[0]}')

icv_empty_values = df[df['ALQ120Q'].apply(lambda x: str(x).strip() == '')]
print(f'Number of rows with empty values: {icv_empty_values.shape[0]}')

# IC: Someone filled out "drinks_per_n" but not "unit"
icv_drinks_per_n_no_unit = df[(df['ALQ120Q'] != '') & (df['ALQ120U'] == '')]
print(f'Number of rows with drinks_per_n but no unit: {icv_drinks_per_n_no_unit.shape[0]}')


# IC: Cases where someone put "999" in the "drinks_per_n" column
icv_drinks_999 = df[df['ALQ120Q'].apply(lambda x: x != '' and int(x) == 999)]
print(f'Number of rows with 999 drinks_per_n: {icv_drinks_999.shape[0]}')



print('--------------')
print('ICVs in cleaned alcohol_consumption_by_age table:')
print('--------------')
df = pd.read_csv('./alcohol_consumption_by_age.csv')
# df = df.fillna('')

print(f'Number of rows: {df.shape[0]}')

icv_empty_values = df[df.apply(lambda x: str(x).strip() == '', axis=1)]
print(f'Number of rows with empty values: {icv_empty_values.shape[0]}')

print(f'Number of rows with drinks_per_n but no unit: N/A, unit column removed')

# IC: invalid "drinks_per_year" values
icv_drinks_999 = df[df['drinks_per_year'].apply(lambda x: x != '' and int(x) >= 999)]
print(f'Number of rows with >=999 drinks_per_year: {icv_drinks_999.shape[0]}')
