from sqlalchemy.dialects.mysql import CHAR, VARCHAR, TEXT
from flask_sqlalchemy import SQLAlchemy
from db.db import db, app, migrate, jwt

class ProfessionalTip(db.Model):
    __tablename__ = 'professional_tips'
    
    id = db.Column(CHAR(36), primary_key=True)
    title = db.Column(VARCHAR(255), nullable=False)
    content = db.Column(TEXT, nullable=False)
    nutritionist_id = db.Column(CHAR(36), db.ForeignKey('nutritionists.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'nutritionist_id': self.nutritionist_id
        }

    def __init__(self, title, content, nutritionist_id):
        self.title = title
        self.content = content
        self.nutritionist_id = nutritionist_id

with app.app_context():
    db.create_all()