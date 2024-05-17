from flask import Blueprint, jsonify, request
from db.db import db, app, migrate, jwt
from models import Nutritionist
from flask_jwt_extended import jwt_required

nutritionist_api = Blueprint('nutritionist_api', __name__)

@nutritionist_api.route('/nutritionists', methods=['GET'])
@jwt_required()
def get_nutritionists():
    nutritionists = Nutritionist.query.all()
    return jsonify([nutritionist.serialize() for nutritionist in nutritionists])

@nutritionist_api.route('/nutritionists/<nutritionist_id>', methods=['GET'])
@jwt_required()
def get_nutritionist(nutritionist_id):
    nutritionist = Nutritionist.query.get(nutritionist_id)
    if nutritionist:
        return jsonify(nutritionist.serialize())
    else:
        return jsonify({'error': 'Nutritionist with id {} not found'.format(nutritionist_id)}), 404

@nutritionist_api.route('/nutritionists', methods=['POST'])
@jwt_required()
def create_nutritionist():
    data = request.json
    new_nutritionist = Nutritionist(**data)
    db.session.add(new_nutritionist)
    db.session.commit()
    return jsonify(new_nutritionist.serialize()), 201

@nutritionist_api.route('/nutritionists/<nutritionist_id>', methods=['PUT'])
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
        return jsonify({'error': 'Nutritionist with id {} not found'.format(nutritionist_id)}), 404

@nutritionist_api.route('/nutritionists/<nutritionist_id>', methods=['DELETE'])
@jwt_required()
def delete_nutritionist(nutritionist_id):
    nutritionist = Nutritionist.query.get(nutritionist_id)
    if nutritionist:
        db.session.delete(nutritionist)
        db.session.commit()
        return jsonify({'message': 'Nutritionist with id {} deleted'.format(nutritionist_id)})
    else:
        return jsonify({'error': 'Nutritionist with id {} not found'.format(nutritionist_id)}), 404