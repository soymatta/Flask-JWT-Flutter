import uuid
from sqlalchemy.dialects.mysql import CHAR, VARCHAR, TEXT, DECIMAL
from flask_sqlalchemy import SQLAlchemy
from db.db import db, app, migrate, jwt


class Nutritionist(db.Model):
    __tablename__ = "nutritionists"

    id = db.Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(VARCHAR(255), nullable=False)
    username = db.Column(VARCHAR(50), unique=True, nullable=False)
    email = db.Column(VARCHAR(255), unique=True, nullable=False)
    password = db.Column(VARCHAR(255), nullable=False)
    description = db.Column(TEXT)
    rating = db.Column(DECIMAL(2, 1), nullable=False, server_default="1.0")
    photo = db.Column(VARCHAR(255))
    instagram = db.Column(VARCHAR(20))
    website = db.Column(VARCHAR(100))
    whatsapp = db.Column(VARCHAR(15))
    skill1 = db.Column(VARCHAR(50), nullable=False)
    skill2 = db.Column(VARCHAR(50))
    skill3 = db.Column(VARCHAR(50))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "description": self.description,
            "rating": self.rating,
            "photo": self.photo,
            "instagram": self.instagram,
            "website": self.website,
            "whatsapp": self.whatsapp,
            "skill1": self.skill1,
            "skill2": self.skill2,
            "skill3": self.skill3,
            "type": "nutritionist",
        }

    professional_tips = db.relationship(
        "ProfessionalTip", backref="nutritionist", lazy=True
    )

    def __init__(
        self,
        name,
        username,
        email,
        password,
        description,
        rating,
        photo,
        instagram,
        website,
        whatsapp,
        skill1,
        skill2,
        skill3,
    ):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.description = description
        self.photo = photo
        self.instagram = instagram
        self.website = website
        self.whatsapp = whatsapp
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3


with app.app_context():
    db.create_all()
