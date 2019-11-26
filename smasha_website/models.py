from .extensions import db

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emails = db.Column(db.String(200), nullable=False, unique=True)