"""Costumer Blueprint."""
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required

from .models import Costumer
from .serializer import CostumerSchema

bp_costumer = Blueprint('costumer', __name__)


@bp_costumer.route('/create-costumer', methods=['POST'])
def register():
    """Register Costumer endpoint."""
    costumer_schema = CostumerSchema()

    costumer, error = costumer_schema(request.json)
    if error:
        return jsonify(error), 401

    current_app.db.session.add(costumer)
    current_app.db.session.commit()

    return costumer_schema.jsonify(costumer), 201


@bp_costumer.route('/costumers', methods=['GET'])
@jwt_required
def show_costumers():
    """List Costumers endpoint."""
    result = Costumer.query.all()
    return CostumerSchema(many=True).jsonify(result), 200


@bp_costumer.route('/delete-costumer/<_id>', methods=['POST'])
@jwt_required
def delete_costumer(_id: int):
    """Delete Costumer endpoint."""
    Costumer.query.filter(Costumer.id == _id).delete()
    current_app.db.session.commit()
    return jsonify('Costumer deleted!')


@bp_costumer.route('/update-costumer/<_id>', methods=['POST'])
@jwt_required
def updade_costumer(_id):
    """Update Costumer endpoint."""
    cs = CostumerSchema()
    query = Costumer.query.filter(Costumer.id == _id)
    query.update(request.json)
    current_app.db.session.commit()
    return cs.jsonify(query.first())
