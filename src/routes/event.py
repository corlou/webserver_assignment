from flask import Blueprint, jsonify, request
from app import db
from models.event import Event, EventSchema

api = Blueprint('event_api', __name__)


@api.route('/events', methods=['GET'])
def list_events():
    ###
    # List all events
    ###
    events = Event.query.order_by(Event.name).all()
    return jsonify(EventSchema(many=True).dump(events))


@api.route('/events', methods=['POST'])
def create_event():
    ###
    # Create event
    ###
    data = request.json

    newEvent = Event(name=data["name"], password=data["password"],
                     email=data["email"], date_of_birth=data["date_of_birth"])
    db.session.add(newEvent)
    db.session.commit()
    return EventSchema().dump(newEvent)


@api.route('/events/<id>', methods=["GET"])
def get_event(id):
    ###
    # Get an event profile
    ###
    event = db.get_or_404(Event, id)
    return EventSchema().dump(event)


@api.route('/events/<id>', methods=["PUT"])
def update_event(id):
    ###
    # Update an event profile
    ###

    # find the event by the id
    event = db.get_or_404(Event, id)

    # update any provided fields
    data = request.json
    if (data.get('name')):
        event.name = data['name']
    if (data.get('email')):
        event.email = data['email']
    if (data.get('date_of_birth')):
        event.date_of_birth = data['date_of_birth']
    db.session.commit()

    # return update event
    return EventSchema().dump(event)


@api.route('/events/<id>', methods=["DELETE"])
def delete_eventid():
    ###
    # Delete a event profile
    ###
    event = db.get_or_404(Event, id)
    db.session.delete(event)
    db.session.commit()
    return 'success'
