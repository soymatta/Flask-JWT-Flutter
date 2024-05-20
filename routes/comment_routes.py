from flask import Blueprint, jsonify, request
from db.db import db, app, migrate, jwt
from models import Comment
from flask_jwt_extended import jwt_required

comment_api = Blueprint("comment_api", __name__)

# CRUD


# GET COMMENTS
@comment_api.route("/comments", methods=["GET"])
def get_comments():
    comments = Comment.query.all()
    return jsonify([comment.serialize() for comment in comments])


# GET COMMENT
@comment_api.route("/comments/<comment_id>", methods=["GET"])
def get_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        return jsonify(comment.serialize())
    else:
        return (
            jsonify({"error": "Comment with id {} not found".format(comment_id)}),
            404,
        )


# CREATE COMMENT
@comment_api.route("/comments", methods=["POST"])
@jwt_required()
def create_comment():
    data = request.json
    new_comment = Comment(**data)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify(new_comment.serialize()), 201


# UPDATE COMMENT
@comment_api.route("/comments/<comment_id>", methods=["PUT"])
@jwt_required()
def update_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        data = request.json
        for key, value in data.items():
            setattr(comment, key, value)
        db.session.commit()
        return jsonify(comment.serialize())
    else:
        return (
            jsonify({"error": "Comment with id {} not found".format(comment_id)}),
            404,
        )


# DELETE COMMENT
@comment_api.route("/comments/<comment_id>", methods=["DELETE"])
@jwt_required()
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        db.session.delete(comment)
        db.session.commit()
        return jsonify({"message": "Comment with id {} deleted".format(comment_id)})
    else:
        return (
            jsonify({"error": "Comment with id {} not found".format(comment_id)}),
            404,
        )
