# Logs Analysis
this project for collecting some information from the news database 
news database has 3 tables 
articles 
author
logs
## installation 
run the database server then run the databse news 

## views added to the database 
to help in the third query 
```
CREATE OR REPLACE VIEW public."timeStatus" AS
SELECT time::date , 
(100*SUM(CASE WHEN status LIKE '404%' then 1 else 0 end) /COUNT(status))AS res
FROM log

GROUP BY time::date
ORDER BY res DESC;


```
## What are the most popular three articles of all time?
```
SELECT title,Count(path) FROM log,Articles 
        where  SUBSTRING(path,10,50)=slug 
        GROUP BY title ORDER BY Count(path) DESC  LIMIT 3
```
## Who are the most popular article authors of all time?

```
SELECT name,COUNT(path)  FROM log,Articles
           INNER JOIN authors ON articles.author=authors.id
           where SUBSTRING(path,10,50)=slug GROUP BY name ORDER BY COUNT(path) DESC
```

## On which days did more than 1% of requests lead to errors?
timeStatus is a view 
```
SELECT * FROM public."timeStatus"
           where res>1
```
