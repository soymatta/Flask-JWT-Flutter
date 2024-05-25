import uuid
from sqlalchemy.dialects.mysql import CHAR, TEXT, VARCHAR, TIMESTAMP
from flask_sqlalchemy import SQLAlchemy
from db.db import app, db


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content = db.Column(TEXT, nullable=False)
    photo = db.Column(TEXT)
    timestamp = db.Column(TIMESTAMP, nullable=False)
    user_id = db.Column(CHAR(36), db.ForeignKey("users.id"), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "photo": self.photo,
            "timestamp": self.timestamp,
            "user_id": self.user_id,
        }

    def __init__(self, content, photo, timestamp, user_id):
        self.content = content
        self.photo = photo
        self.timestamp = timestamp
        self.user_id = user_id


with app.app_context():
    db.create_all()
