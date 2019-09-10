"""DB Models."""
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Costumer(db.Model):
    """Define Costumer table."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def gen_hash(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)


class Product(db.Model):
    """Define Products table."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    brand = db.Column(db.String(255))
    price = db.Column(db.Float)
    review_score = db.Column(db.Float)
    image = db.Column(db.String(255))
