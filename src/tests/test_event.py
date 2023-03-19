import json
from datetime import datetime
from .app import create_test_client
from models.event import EventType

client = create_test_client()

# A fake event we will use to test with
event = {
    "id": None,  # this will be set when we create a event
    "name": "tricks",
    "is_adult": True,
    "teacher_name": "Leeanne",
    "date": "2023-05-05",
    "event_type": EventType.COMPETITION_LOCAL
}


def test_create_event():
    ###
    # POST /events
    ##

    # Send to API
    response = client.post(
        "/events", content_type="application/json", json=event)
    response_json = json.loads(response.data.decode("utf-8"))
    event["id"] = response_json["id"]  # save this for our other tests

    # Check response
    assert response.status_code == 200
    assert response_json["id"] != None
    assert response_json['name'] == event["name"]


def test_update_event():
    ###
    # PUT /events/<id>
    ##

    # Prepare event changes
    event["name"] = "changed name"
    event["date"] = datetime.now()

    # Send to API
    response = client.put(
        "/events/"+str(event["id"]), content_type="application/json", json=event)
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    assert response_json['name'] == event["name"]
    assert response_json['date'] == event["date"].strftime("%Y-%m-%d")


def test_get_event():
    ###
    # GET /events/<id>
    ##

    # Send to API
    response = client.get(
        "/events/"+str(event["id"]), content_type="application/json")
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    assert response_json["id"] == event["id"]


def test_list_events():
    ###
    # GET /events
    ##

    # Send to API
    response = client.get("/events")
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    # there should only be one event in the list
    assert len(response_json) == 1


def test_delete_event():
    ###
    # DELETE /events/<id>
    ##

    # Send to API
    response = client.delete(
        "/events/"+str(event["id"]), content_type="application/json")

    # Check response
    assert response.status_code == 200
