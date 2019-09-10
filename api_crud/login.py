"""Login Blueprint."""
from datetime import timedelta

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token

from .models import Costumer
from .serializer import CostumerSchema

bp_login = Blueprint('login', __name__)


@bp_login.route('/login', methods=['POST'])
def login():
    costumer, error = CostumerSchema().load(request.json)
    if error:
        return jsonify(error), 401

    costumer = Costumer.query.filter_by(email=costumer.email).fisrt()

    if costumer and costumer.verify_password(request.json['password']):
        access_token = create_access_token(
            identity=costumer.id,
            expires_delta=timedelta(seconds=1)
        )
        refresh_token = create_refresh_token(identity=costumer.id)

        return jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'message': 'success'
        }), 200

    return jsonify({
        'message': 'Be sure your credentials are valid'
    }), 401
