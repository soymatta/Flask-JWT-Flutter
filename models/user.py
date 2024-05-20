import uuid
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, TEXT, DECIMAL
from flask_sqlalchemy import SQLAlchemy
from db.db import db, app, migrate, jwt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(VARCHAR(255), unique=True, nullable=False)
    username = db.Column(VARCHAR(50), unique=True, nullable=False)
    password = db.Column(VARCHAR(255), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "type": "user",
        }

    comments = db.relationship("Comment", backref="user", lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


with app.app_context():
    db.create_all()
