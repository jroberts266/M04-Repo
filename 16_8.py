#16.8 assingment
#Author: Joey Roberts
#Date: 2/12/2023
# Using SQLAlchemy


import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
sql = 'select title from book order by title asc'
rows = conn.execute(sql)
for row in rows:
    print(row)
