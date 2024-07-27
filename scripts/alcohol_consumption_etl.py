import sqlite3 
import pandas as pd

# Connect to the sqlite3 database. Query age and alcohol columns.
conn = sqlite3.connect('../clean-data/clean_data.sqlite')
alcohol_df = pd.read_sql_query("""
    SELECT 
        demographic.respondent_seq_no as seqn, 
        demographic.age as age, 
        questionnaire.alcoloh AS drinks_per_n, 
        questionnaire.alcoloh_frequency AS unit 
    FROM demographic
        left join questionnaire on demographic.respondent_seq_no = questionnaire.respondent_seq_no 
""", conn)


# Fill in NaN values with 0
alcohol_df.fillna(0, inplace=True)

# Only keep rows where "unit" is 0,1,2,3
alcohol_df = alcohol_df[alcohol_df['unit'].isin([0,1,2,3])]

# Zero-out rows where the unit is zero
alcohol_df['drinks_per_n'] = alcohol_df.apply(lambda row: 0 if row['unit'] == 0 else row['drinks_per_n'], axis=1)

# Normalize all units to drinks_per_year
def calculate_drinks_per_year(row):
    if row['unit'] == 1:  # Week
        return row['drinks_per_n'] * 52
    elif row['unit'] == 2:  # Month
        return row['drinks_per_n'] * 12
    elif row['unit'] == 3:  # Year
        return row['drinks_per_n']
    else:
        return 0
alcohol_df['drinks_per_year'] = alcohol_df.apply(calculate_drinks_per_year, axis=1)

# Drop the original columns
alcohol_df = alcohol_df.drop(['drinks_per_n', 'unit'], axis=1)

alcohol_df.to_csv('alcohol_consumption_by_age.csv')