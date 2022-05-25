import pdb
from models.book import Book
from models.author import Author


import repositories.author_repository as author_repository
import repositories.book_repository as book_repository


# author_repository.delete_all()
# book_repository.delete_all()

author1= Author("John", "smith")
author_repository.save(author1)

authors=author_repository.select_all()
for author in authors: 
    print (author.__dict__)













pdb.set_trace()