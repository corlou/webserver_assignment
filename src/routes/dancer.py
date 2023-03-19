from flask import Blueprint, jsonify, request
from app import db
from models.dancer import Dancer, DancerSchema

api = Blueprint('dancer_api', __name__)


@api.route('/dancers', methods=['GET'])
def list_dancers():
    ###
    # List all dancers
    ###
    dancers = Dancer.query.order_by(Dancer.name).all()
    return jsonify(DancerSchema(many=True).dump(dancers))


@api.route('/dancers', methods=['POST'])
def create_dancer():
    ###
    # Create dancer
    ###
    data = request.json

    newDancer = Dancer(name=data["name"], password=data["password"],
                       email=data["email"], date_of_birth=data["date_of_birth"])
    db.session.add(newDancer)
    db.session.commit()
    return DancerSchema().dump(newDancer)


@api.route('/dancers/<id>', methods=["GET"])
def get_dancer(id):
    ###
    # Get a dancer profile
    ###
    dancer = db.get_or_404(Dancer, id)
    return DancerSchema().dump(dancer)


@api.route('/dancers/<id>', methods=["PUT"])
def update_dancer(id):
    ###
    # Update a dancer profile
    ###

    # find the dancer by the id
    dancer = db.get_or_404(Dancer, id)

    # update any provided fields
    data = request.json
    if (data.get('name')):
        dancer.name = data['name']
    if (data.get('email')):
        dancer.email = data['email']
    if (data.get('date_of_birth')):
        dancer.date_of_birth = data['date_of_birth']
    db.session.commit()

    # return update dancer
    return DancerSchema().dump(dancer)


@api.route('/dancers/<id>', methods=["DELETE"])
def delete_dancerid():
    ###
    # Delete a dancer profile
    ###
    dancer = db.get_or_404(Dancer, id)
    db.session.delete(dancer)
    db.session.commit()
    return 'success'
   