from flask import Blueprint, jsonify, request
from app import db
from models.registration import Registration, RegistrationSchema

api = Blueprint('registration_api', __name__)


@api.route('/registrations', methods=['GET'])
def list_registrations():
    ###
    # List all registrations
    ###
    registrations = Registration.query.order_by(Registration.name).all()
    return jsonify(RegistrationSchema(many=True).dump(registrations))


@api.route('/registrations', methods=['POST'])
def create_registration():
    ###
    # Create registration
    ###
    data = request.json

    newRegistration = Registration(name=data["name"], password=data["password"],
                                   email=data["email"], date_of_birth=data["date_of_birth"])
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


@api.route('/registrations/<id>', methods=["PUT"])
def update_registration(id):
    ###
    # Update a registration profile
    ###

    # find the registration by the id
    registration = db.get_or_404(Registration, id)

    # update any provided fields
    data = request.json
    if (data.get('name')):
        registration.name = data['name']
    if (data.get('email')):
        registration.email = data['email']
    if (data.get('date_of_birth')):
        registration.date_of_birth = data['date_of_birth']
    db.session.commit()

    # return update registration
    return RegistrationSchema().dump(registration)


@api.route('/registrations/<id>', methods=["DELETE"])
def delete_registrationid():
    ###
    # Delete a registration profile
    ###
    registration = db.get_or_404(Registration, id)
    db.session.delete(registration)
    db.session.commit()
    return 'success'
