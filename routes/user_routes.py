from flask import Blueprint, jsonify, request
from db.db import db, app, migrate, jwt
from models import User
from flask_jwt_extended import jwt_required

user_api = Blueprint('user_api', __name__)

@user_api.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@user_api.route('/users/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.serialize())
    else:
        return jsonify({'error': 'User with id {} not found'.format(user_id)}), 404

@user_api.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    data = request.json
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201

@user_api.route('/users/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = User.query.get(user_id)
    if user:
        data = request.json
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify(user.serialize())
    else:
        return jsonify({'error': 'User with id {} not found'.format(user_id)}), 404

@user_api.route('/users/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User with id {} deleted'.format(user_id)})
    else:
        return jsonify({'error': 'User with id {} not found'.format(user_id)}), 404
