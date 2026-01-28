from flask import Blueprint, request, jsonify
from models.book_model import Book
from database import db
from flask_jwt_extended import get_jwt_identity

book_bp = Blueprint("book_bp", __name__)

# -------------------
# Add Book
# -------------------
@book_bp.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    required = ["id", "title", "author", "year"]
    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    if Book.query.get(data["id"]):
        return jsonify({"error": "Book with this ID already exists"}), 400

    new_book = Book(
        id=data["id"],
        title=data["title"],
        author=data["author"],
        year=data["year"]
    )

    db.session.add(new_book)
    db.session.commit()

    return jsonify({"message": "Book added successfully"}), 201

# -------------------
# Get All Books
# -------------------
@book_bp.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    return jsonify([b.to_dict() for b in books])

# -------------------
# Get Book By ID
# -------------------
@book_bp.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book.to_dict())

# -------------------
# Update Book
# -------------------
@book_bp.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()

    book.title = data.get("title", book.title)
    book.author = data.get("author", book.author)
    book.year = data.get("year", book.year)

    db.session.commit()

    return jsonify({"message": "Book updated successfully"})

# -------------------
# Delete Book
# -------------------
@book_bp.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted successfully"})
