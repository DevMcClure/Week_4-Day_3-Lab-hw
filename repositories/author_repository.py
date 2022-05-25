from db.run_sql import run_sql

from models.book import Book
from models.author import Author



def save(author):
    sql = "INSERT INTO authors (name) VALUES (?) RETURNING *"
    values = [author.name]
    results = run_sql(sql,values)
    id = results[0]['id']
    author.id = id
    return author



def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'])
        author.append(author)
    return authors    




#view 


#create author



# view books


# view book


# create book



# delete book



# edit book


