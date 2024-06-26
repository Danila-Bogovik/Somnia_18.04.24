from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    profile_pic = db.Column(db.String(255), nullable=False)
    about = db.Column(db.Text)
    admin = db.Column(db.Boolean, nullable=False, default=0)
    partner_id = db.Column(db.String(255))
    telegram = db.Column(db.String(255))
    searching_partner = db.Column(db.Boolean, nullable=False, default=0)

class AllowedEmails(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(255), nullable=False) 
    
