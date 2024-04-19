from flask import current_app
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    profile_pic = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text)
    admin = db.Column(db.Boolean, nullable=False, default=0)
    def __repr__(self):
        return f"<User {self.id}: {self.name}>"

class AllowedEmails(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(255), nullable=False) 