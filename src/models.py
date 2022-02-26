import hashlib
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def verify_password(plaintext, ciphertext):
    return plaintext == ciphertext


'''
Business Owner Account
owner, investor
'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    businesses = db.relationship('Business', backref='owner', lazy=True)
    account_type = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'User: {self.id} {self.account_type} {self.username} {self.email} {self.password}'


class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    # location = db.Column(db.String(128), nullable=False)
    # industry = db.Column(db.String(128), nullable=False)
    
    employees = db.Column(db.Integer)
    description = db.Column(db.String(128), nullable=False)

    # date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    
    # owner = db.relationship('User')

    def __repr__(self):
        return f'Business: {self.name} owned by {self.owner_id}'
