# Original Data

This folder includes the original CSV data from the original dataset.


## Variable reference:
The original data uses lots of acronyms for variable names. You can find the reference here:

- demographic: https://wwwn.cdc.gov/Nchs/Nhanes/Search/variablelist.aspx?Component=Demographics&CycleBeginYear=2013
- diet: https://wwwn.cdc.gov/nchs/nhanes/search/variablelist.aspx?Component=Dietary&Cycle=2013-2014
- questionnaire: 


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


## Phase 1 Queries
How many people in the study take insulin?
```
WITH drugs_by_seqn as (
    SELECT seqn, GROUP_CONCAT(rxddrug, ',') as drugs FROM medications GROUP BY seqn
)
SELECT COUNT(*) FROM drugs_by_seqn WHERE drugs like '%INSULIN%';
```

What are the most common drugs taken?
```
SELECT rxddrug, COUNT(*) as count  FROM medications GROUP BY rxddrug order by count desc
```

- Although most of these results look decent, you can see some medications that seem irregular. For example, 62 people claim to take the medication "99999". And 6 people take "55555".
- Additionally, there are some cases of different names being used for the same drug. e.g. "Insulin" and "Insulin Regular" are probably the same medication.


What is the average age of participant?
```
SELECT min(cast(ridageyr as integer)), max(cast(ridageyr as integer)), avg(cast(ridageyr as integer)) FROM demographic where ridageyr is not null;

SELECT min(cast(ridexagm as integer)), max(cast(ridexagm as integer)), avg(cast(ridexagm as integer)) FROM demographic where ridexagm is not null;
```

- The age of participants in the original dataset is actually split between 2 columns, rideageyr and ridexagm, for participants over 19-or-older and 18-and-younger. This makes it pretty difficult to calculate the average age with just a SQL query.

- To make the query even harder, the 18-and-younger group is measured in months, whereas the 19-and-older gorup is measured in years.

What is the relationship betwen age, and use of alcohol and tobaacco, or other drugs?
```
SELECT 
    demographic.seqn as seqn, 
    demographic.ridageyr as age, 
    questionnaire.ALQ120Q AS drinks_per_n, 
    questionnaire.ALQ120U AS unit 
FROM demographic
    left join questionnaire on demographic.seqn = questionnaire.seqn 
WHERE drinks_per_n IS NOT NULL
LIMIT 10;

# Note: in the "drinks_per_n" column, 777 = refused, 999 = dont know
# Note: in the "unit" column, 1 = /week, 2 = /month, 3=/year, 7 = refused, 9 = dont know
```

- This is another query that's almost impossible to answer with plain SQL, because the unit of measurement is dynamic.
To get a realistic answer to this query, we'd have to normalize all the "drinks_per_n" column against the "unit" column, multiplying everything by some factor to get a comparable value.



What is the average weight of survey participants?
```
SELECT AVG(WHD020) FROM questionnaire;
```

- This query gives `160.649`, which seems reasonable. However, doign another query `SELECT WHD020 FROM questionnaire WHERE CAST(WHD020 AS INTEGER) > 500;` shows many values of "9999" and "7777". These were probably used by the research team to indicaate special cases, like "refused to answer". They need to be filtered out of the actual calculation.