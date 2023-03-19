from flask import Blueprint
from flask import jsonify, make_response

api = Blueprint('root_api', __name__)


@api.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Pole Calendar API'})


@api.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Route does not exist'}), 404)


@api.errorhandler(500)
def server_error():
    return make_response(jsonify({'error': 'Internal server error'}), 500)
