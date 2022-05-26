import pdb
from models.book import Book
from models.author import Author


import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


# author_repository.delete_all()
# book_repository.delete_all()

author_1= Author("John", "smith")
author_repository.save(author_1)

authors=author_repository.select_all()
for author in authors: 
    print (author.__dict__)



book_1= Book(author_1, "The best book ever")
book_repository.save(book_1)


# book = book_repository.select(id)



books = book_repository.select_all()
for book in books:
    print (book.__dict__)
















pdb.set_trace()