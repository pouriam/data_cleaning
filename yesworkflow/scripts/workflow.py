# @BEGIN NHANES_Data_Cleaning
# @IN demographic.csv @URI file:original-data/demographic.csv
# @IN diet.csv  @URI file:original-data/diet.csv
# @IN examination.csv  @URI file:original-data/examination.csv
# @IN labs.csv  @URI file:original-data/labs.csv
# @IN medications.csv  @URI file:original-data/medications.csv
# @IN questionnaire.csv  @URI file:original-data/questionnaire.csv
# @OUT original_data_sqlite  @URI file:original-data/original_data.sqlite
# @OUT clean_data_sqlite  @URI file:clean-data/clean_data.sqlite
# @OUT alcohol_consumption_by_age @URI file:scripts/alcohol_consumption_by_age.csv 
# @OUT medications_exploded @URI file:scripts/medications_exploded.csv 
# @Out icv_report

    # @BEGIN OpenRefine
    # @IN demographic.csv
    # @IN diet.csv  
    # @IN examination.csv  
    # @IN labs.csv  
    # @IN medications.csv  
    # @IN questionnaire.csv  
    # @OUT demographic_sql_cleaned  @URI file:clean-data/demographic.sql
    # @OUT diet_sql_cleaned  @URI file:clean-data/diet.sql
    # @OUT examination_sql_cleaned  @URI file:clean-data/examination.sql
    # @OUT labs_sql_cleaned  @URI file:clean-data/labs.sql
    # @OUT medications_sql_cleaned  @URI file:clean-data/medications.sql
    # @OUT questionnaire_sql_cleaned  @URI file:clean-data/questionnaire.sql

    # @END OpenRefine

    # @BEGIN Sqlite3_Original
    # @IN demographic.csv
    # @IN diet.csv  
    # @IN examination.csv  
    # @IN labs.csv  
    # @IN medications.csv  
    # @IN questionnaire.csv  
    # @OUT original_data_sqlite  @URI file:original-data/original_data.sqlite
    # @END Sqlite3_Original

    # @BEGIN Sqlite3_Clean
    # @IN demographic_sql_cleaned  @URI file:clean-data/demographic.sql
    # @IN diet_sql_cleaned  @URI file:clean-data/diet.sql
    # @IN examination_sql_cleaned  @URI file:clean-data/examination.sql
    # @IN labs_sql_cleaned  @URI file:clean-data/labs.sql
    # @IN medications_sql_cleaned  @URI file:clean-data/medications.sql
    # @IN questionnaire_sql_cleaned  @URI file:clean-data/questionnaire.sql
    # @OUT clean_data_sqlite  @URI file:clean-data/clean_data.sqlite
    # @END Sqlite3_Clean


    # @BEGIN medications_etl.py
    # @IN clean_data_sqlite 
    # @OUT medications_exploded @URI file:scripts/medications_exploded.csv 
    # @END medications_etl.py

    # @BEGIN alcohol_consumption_etl.py
    # @IN clean_data_sqlite 
    # @OUT alcohol_consumption_by_age @URI file:scripts/alcohol_consumption_by_age.csv 
    # @END alcohol_consumption_etl.py

    # @BEGIN icvs.py
    # @IN medications.csv 
    # @IN demographic.csv
    # @IN questionnaire.csv
    # @IN medications_exploded
    # @IN alcohol_consumption_by_age
    # @OUT icv_report
    # @END icvs.py

# @END NHANES_Data_Cleaning