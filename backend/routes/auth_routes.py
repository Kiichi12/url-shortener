from flask import Blueprint, request, jsonify
from models.user_model import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.find_by_email(email):
        return jsonify({"error": "User already exists"}), 400

    User.create_user(username, email, password)
    return jsonify({"message": "User registered successfully"}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.find_by_email(email)
    if user and user['password'] == password:  # In production, use password hashing!
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401