from flask import Blueprint, jsonify, request
from app import db
from models.favourite import Favourite, FavouriteSchema

api = Blueprint('favourite_api', __name__)


@api.route('/favourites', methods=['GET'])
def list_favourite():
    ###
    # List all favourites
    ###
    favourite = Favourite.query.order_by(Favourite.name).all()
    return jsonify(FavouriteSchema(many=True).dump(favourite))


@api.route('/favourites', methods=['POST'])
def create_favourite():
    ###
    # Create favourite
    ###
    data = request.json

    newFavourite = Favourite(name=data["name"], password=data["password"],
                             email=data["email"], date_of_birth=data["date_of_birth"])
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
    # Update a favourite profile
    ###

    # find the favourite by the id
    favourite = db.get_or_404(Favourite, id)

    # update any provided fields
    data = request.json
    if (data.get('name')):
        favourite.name = data['name']
    if (data.get('email')):
        favourite.email = data['email']
    if (data.get('date_of_birth')):
        favourite.date_of_birth = data['date_of_birth']
    db.session.commit()

    # return update favourite
    return FavouriteSchema().dump(favourite)


@api.route('/favourites/<id>', methods=["DELETE"])
def delete_favouriteid():
    ###
    # Delete a favourite
    ###
    favourite = db.get_or_404(Favourite, id)
    db.session.delete(favourite)
    db.session.commit()
    return 'success'
