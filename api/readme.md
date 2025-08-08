# Simple Books API

## Product Requirements Document (PRD)

### 1. Overview
The Simple Books API is a minimal Flask-based backend that provides book information through HTTP GET requests. It is designed as a beginner-friendly example for learning how to build RESTful APIs using Python and Flask.

### 2. Goals & Objectives
- Demonstrate how to build a simple API using Flask.
- Provide GET endpoints for retrieving all books and a single book by ID.
- Use static (hardcoded) data for simplicity.
- Serve as a base for future enhancements (e.g., database integration, more endpoints).

### 3. Scope

#### In Scope
- **Backend only:** Python 3.x and Flask.
- **Static dataset:** 3 books stored in a Python list.
- **Endpoints:**
  - `/` – Returns a friendly “API is running” message.
  - `/api/books` – Returns a JSON array of all books.
  - `/api/books/<id>` – Returns JSON details of a specific book.
- **JSON format:** All responses are in JSON.
- **Error handling:** Returns a 404 and error message if a book is not found.

#### Out of Scope
- No database or persistent storage.
- No authentication or authorization.
- No POST, PUT, DELETE, or PATCH endpoints.
- No frontend or documentation UI.

### 4. Functional Requirements

| ID   | Requirement                                                                 |
|------|-----------------------------------------------------------------------------|
| FR1  | The API must return a friendly message at the root endpoint `/`.            |
| FR2  | The API must return all books as a JSON array at `/api/books`.              |
| FR3  | The API must return a single book by ID at `/api/books/<id>`.               |
| FR4  | The API must return a 404 error and JSON error message if book not found.   |
| FR5  | The API must use only Python 3.x and Flask.                                 |

### 5. Non-Functional Requirements

- **Performance:** Should respond within 500ms under normal conditions.
- **Reliability:** Should not crash on invalid input; must handle errors gracefully.
- **Maintainability:** Code should be clear, well-commented, and easy to extend.
- **Portability:** Should run on any system with Python 3.x and Flask installed.

### 6. Success Metrics

- API returns correct data for all endpoints.
- Error handling works as expected.
- Code is readable and easy to modify.
- Can be run locally with minimal setup.

### 7. Future Considerations

- Add support for POST, PUT, DELETE methods.
- Integrate with a database for persistent storage.
- Add authentication and authorization.
- Provide API documentation (Swagger/OpenAPI).
- Add pagination and filtering for book lists.

---

## Example Usage

### Get API Status
```
GET /
Response: "API is running. Try /api/books or api/books/2"
```

### Get All Books
```
GET /api/books
Response:
[
  {"id": 1, "title": "Python Crash Course", "author": "Eric Matthes"},
  {"id": 2, "title": "Clean Code", "author": "Robert C. Martin"},
  {"id": 3, "title": "Fluent Python", "author": "Luciano Ramalho"}
]
```

### Get Book by ID
```
GET /api/books/2
Response:
{"id": 2, "title": "Clean Code", "author": "Robert C. Martin"}
```

### Book Not Found
```
GET /api/books/99
Response:
{"error": "Book not found"}
Status: 404
```

---

## How to Run

1. Install dependencies:
   ```
   pip install flask
   ```
2. Run the app:
   ```
   python app.py
   ```
3. Access the API at [http://localhost:5000](http://localhost:5000)

---
