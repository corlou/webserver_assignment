from flask import Blueprint, jsonify, request
from app import db
from models.studio import Studio, StudioSchema

api = Blueprint('studio_api', __name__)


@api.route('/studios', methods=['GET'])
def list_studios():
    ###
    # List all studios
    ###
    studios = Studio.query.order_by(Studio.name).all()
    return jsonify(StudioSchema(many=True).dump(studios))


@api.route('/studios', methods=['POST'])
def create_studio():
    ###
    # Create studio
    ###
    data = request.json

    newStudio = Studio(name=data["name"], password=data["password"],
                       email=data["email"], date_of_birth=data["date_of_birth"])
    db.session.add(newStudio)
    db.session.commit()
    return StudioSchema().dump(newStudio)


@api.route('/studios/<id>', methods=["GET"])
def get_studio(id):
    ###
    # Get a studio profile
    ###
    studio = db.get_or_404(Studio, id)
    return StudioSchema().dump(studio)


@api.route('/studios/<id>', methods=["PUT"])
def update_studio(id):
    ###
    # Update a studio profile
    ###

    # find the studio by the id
    studio = db.get_or_404(Studio, id)

    # update any provided fields
    data = request.json
    if (data.get('name')):
        studio.name = data['name']
    if (data.get('email')):
        studio.email = data['email']
    if (data.get('date_of_birth')):
        studio.date_of_birth = data['date_of_birth']
    db.session.commit()

    # return update studio
    return StudioSchema().dump(studio)


@api.route('/studios/<id>', methods=["DELETE"])
def delete_studioid():
    ###
    # Delete a studio profile
    ###
    studio = db.get_or_404(Studio, id)
    db.session.delete(studio)
    db.session.commit()
    return 'success'
