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

    newEvent = Event(name=data["name"], is_adult=data["is_adult"],
                     event_type=data["event_type"],
                     teacher_name=data["teacher_name"],
                     date=data["date"])
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
    if (data.get('is_adult')):
        event.is_adult = data['is_adult']
    if (data.get('event_type')):
        event.event_type = data['event_type']
    if (data.get('teacher_name')):
        event.teacher_name = data['teacher_name']
    if (data.get('date')):
        event.date = data['date']
    db.session.commit()

    # return update event
    return EventSchema().dump(event)


@api.route('/events/<id>', methods=["DELETE"])
def delete_event(id):
    ###
    # Delete a event profile
    ###
    event = db.get_or_404(Event, id)
    db.session.delete(event)
    db.session.commit()
    return 'success'
