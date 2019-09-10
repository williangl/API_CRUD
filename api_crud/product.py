"""Product Blueprint."""
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required

from .models import Product
from .serializer import ProductSchema

bp_product = Blueprint('product', __name__)


@bp_product.route('/create-product', methods=['POST'])
def register_product():
    """Register Product endpoint."""
    product_schema = ProductSchema()

    product, error = product_schema(request.json)
    if error:
        return jsonify(error), 401

    current_app.db.session.add(product)
    current_app.db.session.commit()

    return product_schema.jsonify(product), 201


@bp_product.route('/products', methods=['GET'])
@jwt_required
def show_products():
    """List Product endpoint."""
    result = Product.query.all()
    return ProductSchema(many=True).jsonify(result), 200


@bp_product.route('/delete-costumer/<_id>', methods=['POST'])
@jwt_required
def delete_costumer(_id: int):
    """Delete Product endpoint."""
    Product.query.filter(Product.id == _id).delete()
    current_app.db.session.commit()
    return jsonify('Product deleted!')


@bp_product.route('/update-product/<_id>', methods=['POST'])
@jwt_required
def updade_product(_id):
    """Update Product endpoint."""
    ps = ProductSchema()
    query = Product.query.filter(Product.id == _id)
    query.update(request.json)
    current_app.db.session.commit()
    return ps.jsonify(query.first())
