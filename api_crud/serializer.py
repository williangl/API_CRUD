from flask_marshmallow import Marshmallow
from marshmallow import fields, validates, ValidationError
from .models import Costumer, Product


ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class CostumerSchema(ma.ModelSchema):
    class Meta:
        model = Costumer

    name = fields.Str(required=True)
    email = fields.Str(required=True)

    @validates('id')
    def validade_id(self, value):
        raise ValidationError('Do not send your ID')


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
