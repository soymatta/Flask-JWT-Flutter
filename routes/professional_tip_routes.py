from flask import Blueprint, jsonify, request
from db.db import db, app, migrate, jwt
from models import ProfessionalTip
from flask_jwt_extended import jwt_required

professional_tip_api = Blueprint('professional_tip_api', __name__)

@professional_tip_api.route('/professional_tips', methods=['GET'])
def get_professional_tips():
    professional_tips = ProfessionalTip.query.all()
    return jsonify([professional_tip.serialize() for professional_tip in professional_tips])

@professional_tip_api.route('/professional_tips/<professional_tip_id>', methods=['GET'])
def get_professional_tip(professional_tip_id):
    professional_tip = ProfessionalTip.query.get(professional_tip_id)
    if professional_tip:
        return jsonify(professional_tip.serialize())
    else:
        return jsonify({'error': 'Professional Tip with id {} not found'.format(professional_tip_id)}), 404

@professional_tip_api.route('/professional_tips', methods=['POST'])
@jwt_required()
def create_professional_tip():
    data = request.json
    new_professional_tip = ProfessionalTip(**data)
    db.session.add(new_professional_tip)
    db.session.commit()
    return jsonify(new_professional_tip.serialize()), 201

@professional_tip_api.route('/professional_tips/<professional_tip_id>', methods=['PUT'])
@jwt_required()
def update_professional_tip(professional_tip_id):
    professional_tip = ProfessionalTip.query.get(professional_tip_id)
    if professional_tip:
        data = request.json
        for key, value in data.items():
            setattr(professional_tip, key, value)
        db.session.commit()
        return jsonify(professional_tip.serialize())
    else:
        return jsonify({'error': 'Professional Tip with id {} not found'.format(professional_tip_id)}), 404

@professional_tip_api.route('/professional_tips/<professional_tip_id>', methods=['DELETE'])
@jwt_required()
def delete_professional_tip(professional_tip_id):
    professional_tip = ProfessionalTip.query.get(professional_tip_id)
    if professional_tip:
        db.session.delete(professional_tip)
        db.session.commit()
        return jsonify({'message': 'Professional Tip with id {} deleted'.format(professional_tip_id)})
    else:
        return jsonify({'error': 'Professional Tip with id {} not found'.format(professional_tip_id)}), 404
