#!/usr/bin/env python3
import psycopg2

try:
    conn = psycopg2.connect(database="news")  # database connection

    print("Database Connected....")
    cur = conn.cursor()

    # most popular three articles
    cur.execute(
        """SELECT title,Count(path) FROM log,Articles
        where  SUBSTRING(path,10,50)=slug
        GROUP BY title ORDER BY Count(path) DESC  LIMIT 3  """)

    rows = cur.fetchall()
    print("What are the most popular three articles of all time?\n")
    for row in rows:
        print(row[0], ' - ', row[1], 'Views')
    # most popular article author
    cur.execute(
        """SELECT name,COUNT(path)  FROM log,Articles
           JOIN authors ON articles.author=authors.id
           where SUBSTRING(path,10,50)=slug
           GROUP BY name ORDER BY COUNT(path) DESC  """)
    rows = cur.fetchall()
    print("\nWho are the most popular article authors of all time?\n")
    for row in rows:
        print(row[0], ' - ', row[1], 'Views')

    # On which days did more than 1% of requests lead to errors?
    cur.execute(
        """SELECT * FROM public."timeStatus"
           where res>1""")
    rows = cur.fetchall()
    print("\nOn which days did more than 1% of requests lead to errors?\n")
    for row in rows:
        print(row[0], ' - ', row[1], '% errors')
except Exception:
    print("error in the database")
