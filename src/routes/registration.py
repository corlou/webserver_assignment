from flask import Blueprint, jsonify, request
from app import db
from models.registration import Registration, RegistrationSchema

api = Blueprint('registration_api', __name__)


@api.route('/registrations', methods=['GET'])
def list_registrations():
    ###
    # List all registrations
    ###
    registrations = Registration.query.order_by(Registration.event_id).all()
    return jsonify(RegistrationSchema(many=True).dump(registrations))


@api.route('/registrations', methods=['POST'])
def create_registration():
    ###
    # Create registration
    ###
    data = request.json

    newRegistration = Registration(
        dancer_id=data["dancer_id"],
        event_id=data["event_id"],
        date_registered=data["date_registered"]
    )
    db.session.add(newRegistration)
    db.session.commit()
    return RegistrationSchema().dump(newRegistration)


@api.route('/registrations/<id>', methods=["GET"])
def get_registration(id):
    ###
    # Get a registration profile
    ###
    registration = db.get_or_404(Registration, id)
    return RegistrationSchema().dump(registration)


@api.route('/registrations/<id>', methods=["DELETE"])
def delete_registration(id):
    ###
    # Delete a registration profile
    ###
    registration = db.get_or_404(Registration, id)
    db.session.delete(registration)
    db.session.commit()
    return 'success'
