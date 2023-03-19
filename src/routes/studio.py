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

    newStudio = Studio(name=data["name"], street_num=data["street_num"],
                       street_name=data["street_name"], postcode=data["postcode"], contact_num=data["contact_num"])
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
    if (data.get('street_num')):
        studio.street_num = data['street_num']
    if (data.get('street_name')):
        studio.street_name = data['street_name']
    if (data.get('postcode')):
        studio.postcode = data['postcode']
    if (data.get('contact_num')):
        studio.contact_num = data['contact_num']
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
