from flask import Flask, render_template, request
from repositories import book_repository
from repositories import author_repository
from models.author import Author
from models.book import Book
from flask import Blueprint 


books_blueprint = Blueprint("books", __name__)



@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books=books)