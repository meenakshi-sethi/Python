# creating a simple API (backend)

from flask import Flask, jsonify

app = Flask(__name__)

# Sample data 
books = [
    {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 3, "title": "Fluent Python", "author": "Luciano Ramalho"}
]

# API endpoints

# Root friendly msg
@app.route("/")
def home():
    return "API is running. Try /api/books or api/books/2"

# GET All 
@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)

# GET Item
@app.route("/api/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)