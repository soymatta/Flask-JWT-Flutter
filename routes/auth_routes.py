from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from db.db import db, app, migrate, jwt
from models import User, Nutritionist

auth_api = Blueprint("auth_api", __name__)


@auth_api.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    nutritionist = Nutritionist.query.filter_by(username=username).first()

    if user and user.password == password:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token, type="user"), 200
    elif nutritionist and nutritionist.password == password:
        access_token = create_access_token(identity=nutritionist.id)
        return jsonify(access_token=access_token, type="nutritionist"), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
