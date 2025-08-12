# creating a simple API (backend)

from flask import Flask, jsonify, request
# ...existing code...
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data 
books = [
    {"id": 1, "title": "Python Crash Course1", "author": "Eric Matthes"},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
    {"id": 3, "title": "Fluent Python", "author": "Luciano Ramalho"}
]

# API endpoints

# Root friendly msg
@app.route("/")
def home():
    return "<h1>API is running. Try /api/books or api/books/2</h1>"

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

# POST: Add a new book
@app.route("/api/books", methods = ["POST"])
def add_book():
    data = request.get_json()
    if not data or not all(k in data for k in ("title", "author")):
        return jsonify({ "error": "Title and author required"}), 400
    new_id = max([b["id"] for b in books], default=0) + 1
    new_book = {
        "id": new_id,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT: Update an existing book
@app.route("/api/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    book["title"] = data.get("title", book["title"])
    book["author"] = data.get("author", book["author"])
    return jsonify(book)
    return jsonify(book)


if __name__ == "__main__":
    app.run(debug=True)