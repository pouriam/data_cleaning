# Original Data

This folder includes the original CSV data from the original dataset.


## Querying via sqlite3

The file `original_data.sqlite` includes all the CSV files, directly imported to sqlite3 using the following steps:

1. Start an interactive sqlite3 shell
    ```
    sqlite3 original_data.sqlite
    ```

2. In that shell, use the `.import` command to import all of the csv files
    ```
    .import demographic.csv demographic --csv
    .import diet.csv diet --csv
    .import examination.csv examination --csv
    .import labs.csv labs --csv
    .import medications.csv medications --csv
    .import questionnaire.csv questionnaire --csv
    ```

