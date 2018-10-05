import psycopg2

# class PSQLAdapter():
address = "asdfsaf"
con = psycopg2.connect("dbname='test' user='test' host='localhost' password='123456' port=5000")
cur = con.cursor()

cur.execute("CREATE TABLE test(id serial PRIMARY KEY, name varchar, email varchar)")

con.commit()