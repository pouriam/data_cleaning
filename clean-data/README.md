# Phase 2 Queries

How many people in the study are taking 1 drug, 2 drugs, 3 drugs?
```
select drug_name1, count(*) as count from medications group by drug_name1 order by count desc;
select drug_name2, count(*) as count from medications group by drug_name2 order by count desc limit 200;
select drug_name3, count(*) as count from medications group by drug_name3 order by count desc limit 300;
select drug_name4, count(*) as count from medications group by drug_name4 order by count desc limit 400;
```