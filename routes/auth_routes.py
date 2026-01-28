from flask import Blueprint, request, jsonify
from models.user_model import User
from database import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth_bp", __name__)

# Register
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "User already exists"}), 400

    role = data.get("role", "user")

    hashed_pw = generate_password_hash(data["password"]).decode("utf-8")

    user = User(
        username=data["username"],
        password=hashed_pw,
        role=role
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={
    "id": user.id,
    "role": user.role
})

    return jsonify({"access_token": token})
