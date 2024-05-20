from flask import Blueprint, jsonify, request
from db.db import db, app, migrate, jwt
from models import Nutritionist
from flask_jwt_extended import jwt_required

nutritionist_api = Blueprint("nutritionist_api", __name__)

# CRUD


# GET NUTRITIONISTS
@nutritionist_api.route("/nutritionists", methods=["GET"])
@jwt_required()
def get_nutritionists():
    nutritionists = Nutritionist.query.all()
    return jsonify([nutritionist.serialize() for nutritionist in nutritionists])


# GET NUTRITIONIST
@nutritionist_api.route("/nutritionists/<nutritionist_id>", methods=["GET"])
@jwt_required()
def get_nutritionist(nutritionist_id):
    nutritionist = Nutritionist.query.get(nutritionist_id)
    if nutritionist:
        return jsonify(nutritionist.serialize())
    else:
        return (
            jsonify(
                {"error": "Nutritionist with id {} not found".format(nutritionist_id)}
            ),
            404,
        )


# UPDATE NUTRITIONIST
@nutritionist_api.route("/nutritionists/<nutritionist_id>", methods=["PUT"])
@jwt_required()
def update_nutritionist(nutritionist_id):
    nutritionist = Nutritionist.query.get(nutritionist_id)
    if nutritionist:
        data = request.json
        for key, value in data.items():
            setattr(nutritionist, key, value)
        db.session.commit()
        return jsonify(nutritionist.serialize())
    else:
        return (
            jsonify(
                {"error": "Nutritionist with id {} not found".format(nutritionist_id)}
            ),
            404,
        )


# DELETE NUTRITIONIST
@nutritionist_api.route("/nutritionists/<nutritionist_id>", methods=["DELETE"])
@jwt_required()
def delete_nutritionist(nutritionist_id):
    nutritionist = Nutritionist.query.get(nutritionist_id)
    if nutritionist:
        db.session.delete(nutritionist)
        db.session.commit()
        return jsonify(
            {"message": "Nutritionist with id {} deleted".format(nutritionist_id)}
        )
    else:
        return (
            jsonify(
                {"error": "Nutritionist with id {} not found".format(nutritionist_id)}
            ),
            404,
        )


# REGISTER NUTRITIONIST
@nutritionist_api.route("/nutritionists/register", methods=["POST"])
def register_nutritionist():
    data = request.json

    fields = ["name", "username", "email", "instagram"]
    for field in fields:
        if Nutritionist.query.filter_by(**{field: data.get(field)}).first():
            return (
                jsonify({"error": f"Nutritionist with {field} already exists"}),
                400,
            )

    new_nutritionist = Nutritionist(**data)
    db.session.add(new_nutritionist)
    db.session.commit()
    return jsonify(new_nutritionist.serialize()), 201
