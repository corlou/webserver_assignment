from flask import Blueprint, jsonify, request
from app import db
from models.favourite import Favourite, FavouriteSchema

api = Blueprint('favourite_api', __name__)


@api.route('/favourites', methods=['GET'])
def list_favourite():
    ###
    # List all favourites
    ###
    favourite = Favourite.query.order_by(Favourite.id).all()
    return jsonify(FavouriteSchema(many=True).dump(favourite))


@api.route('/favourites', methods=['POST'])
def create_favourite():
    ###
    # Create favourite
    ###
    data = request.json

    newFavourite = Favourite(
        dancer_id=data["dancer_id"], event_id=data["event_id"])
    db.session.add(newFavourite)
    db.session.commit()
    return FavouriteSchema().dump(newFavourite)


@api.route('/favourites/<id>', methods=["GET"])
def get_favourite(id):
    ###
    # Get a favourite
    ###
    favourite = db.get_or_404(Favourite, id)
    return FavouriteSchema().dump(favourite)


@api.route('/favourites/<id>', methods=["PUT"])
def update_favourite(id):
    ###
    # Update a favourite
    ###

    # find the favourite by the id
    favourite = db.get_or_404(Favourite, id)

    # update any provided fields
    data = request.json
    if (data.get('dancer_id')):
        favourite.dancer_id = data['dancer_id']
    if (data.get('event_id')):
        favourite.event_id = data['event_id']
    db.session.commit()

    # return update favourite
    return FavouriteSchema().dump(favourite)


@api.route('/favourites/<id>', methods=["DELETE"])
def delete_favourite(id):
    ###
    # Delete a favourite
    ###
    favourite = db.get_or_404(Favourite, id)
    db.session.delete(favourite)
    db.session.commit()
    return 'success'
