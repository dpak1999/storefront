from sqlalchemy.orm import validates
from storefront.extension import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(150), nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        if len(name.strip()) <= 3:
            raise ValueError("Needs to have a real name")
        return name
