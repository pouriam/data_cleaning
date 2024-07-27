## Transform Medications

This script splits the 4 drug1, drug2, drug3, drug4 columns into a single "drug_name" column, with a new row for each drug taken by a single survey respondent.

This will allow us to more easily count the number of drugs being taken by all participants of the study, without having to query 4 differnt columns and add the results.

```
python ./transform_medications.py
```

Then, in a sqlite3 session
```
.headers on
.mode column

.import medications_exploded.csv medications_exploded --csv

SELECT drug_name, COUNT(*) AS count 
FROM medications_exploded 
WHERE drug_name != '' 
GROUP BY drug_name 
ORDER BY count DESC
LIMIt 5;
```


## Alcohol usage by age
```
python ./alcohol_consumption_by_age.py
```

Then in sqlite3
```
.headers on
.mode column

.import alcohol_consumption_by_age.csv alcohol_consumption_by_age --csv

SELECT age, AVG(drinks_per_year) FROM alcohol_consumption_by_age GROUP BY age ORDER BY CAST(age AS INTEGER) desc;
SELECT age, AVG(drinks_per_year) as dpy FROM alcohol_consumption_by_age  GROUP BY age ORDER BY dpy desc;
```