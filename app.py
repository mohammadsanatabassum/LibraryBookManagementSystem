from flask import Flask
from database import db
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Blueprints
from routes.book_routes import book_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)

# ------------------------
# Configuration
# ------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# ------------------------
# Initialize Extensions
# ------------------------
db.init_app(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# ------------------------
# Import Models
# ------------------------
from models.book_model import Book
from models.user_model import User

# ------------------------
# Create Tables
# ------------------------
with app.app_context():
    db.create_all()

# ------------------------
# Register Blueprints
# ------------------------
app.register_blueprint(book_bp)
app.register_blueprint(auth_bp)

# ------------------------
# Home Route
# ------------------------
@app.route("/")
def home():
    return "Library Book Management System API Running!"

# ------------------------
# Run Server
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
