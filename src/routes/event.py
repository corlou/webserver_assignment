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
    # Create an event
    ###
    data = request.json

    newEvent = Event(name=data["title"], is_adult=data["adult"],
                     event=data["type"], teacher_name=data["instructor"], date=data["date"])
    db.session.add(newEvent)
    db.session.commit()
    return EventSchema().dump(newEvent)


@api.route('/events/<id>', methods=["GET"])
def get_event(id):
    ###
    # Get the detials of an event
    ###
    event = db.get_or_404(Event, id)
    return EventSchema().dump(event)


@api.route('/events/<id>', methods=["PUT"])
def update_event(id):
    ###
    # Update an event
    ###

    # find the event by the id
    event = db.get_or_404(Event, id)

    # update any provided fields
    data = request.json
    if (data.get('name')):
        event.name = data['title']
    if (data.get('adult')):
        event.adult = data['adult']
    if (data.get('type')):
        event.type = data['type']
    if (data.get('instructor')):
        event.instructor = data['instructor']
    if (data.get('date')):
        event.date = data['date']
    db.session.commit()

    # return update dancer
    return EventSchema().dump(event)


@api.route('/dancers/<id>', methods=["DELETE"])
def delete_event():
    ###
    # Delete an event
    ###
    event = db.get_or_404(Event, id)
    db.session.delete(event)
    db.session.commit()
    return 'success'
