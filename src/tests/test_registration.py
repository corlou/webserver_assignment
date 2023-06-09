import json
from .app import create_test_client
from models.event import EventType

client = create_test_client()

# A fake studio we will use to test with
studio = {
    "id": None,  # this will be set when we create a studio
    "name": "Csolta",
    "street_num": "123",
    "street_name": "Moggill Road",
    "postcode": 4068,
    "contact_num": "0411222333",
}

# A fake dancer we will use to test with
dancer = {
    "id": None,  # this will be set when we create a dancer
    "name": "zoe",
    "password": "password",
    "email": "zoe@example.com",
    "date_of_birth": "1990-01-01",
    "studio_id": None
}

# A fake event we will use to test with
event = {
    "id": None,  # this will be set when we create a event
    "name": "tricks",
    "is_adult": True,
    "teacher_name": "Leeanne",
    "date": "2023-05-05",
    "event_type": EventType.COMPETITION_LOCAL
}

# A fake favourite we will use to test with
# Note: all empty IDs will be set when we create the test data
registration = {
    "id": None,
    "dancer_id": None,
    "event_id": None,
    "date_registered": "2023-05-05"
}


def test_create_relations():
    ###
    # This sets up the db with the relations we need to test
    # the registrations
    ###
    # Studio
    studio_response = client.post(
        "/studios", content_type="application/json", json=studio)
    studio_response_json = json.loads(studio_response.data.decode("utf-8"))
    dancer["studio_id"] = studio_response_json["id"]
    # Dancer
    dancer_response = client.post(
        "/dancers", content_type="application/json", json=dancer)
    dancer_response_json = json.loads(dancer_response.data.decode("utf-8"))
    # Event
    event_response = client.post(
        "/events", content_type="application/json", json=event)
    event_response_json = json.loads(event_response.data.decode("utf-8"))
    # Populate the test entities
    studio["id"] = studio_response_json["id"]
    dancer["id"] = dancer_response_json["id"]
    event["id"] = event_response_json["id"]
    registration["dancer_id"] = dancer["id"]
    registration["event_id"] = event["id"]
    # Check that our test records got created
    assert dancer_response.status_code == 200
    assert event_response.status_code == 200


def test_create_registration():
    ###
    # POST /registrations
    ##

    # Send to API
    response = client.post(
        "/registrations", content_type="application/json", json=registration)
    response_json = json.loads(response.data.decode("utf-8"))
    # save this for our other tests
    registration["id"] = response_json["id"]

    # Check response
    assert response.status_code == 200
    assert response_json["id"] != None


def test_get_registration():
    ###
    # GET /registrations/<id>
    ##

    # Send to API
    response = client.get(
        "/registrations/"+str(registration["id"]), content_type="application/json")
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    assert response_json["id"] == registration["id"]


def test_list_registrations():
    ###
    # GET /registrations
    ##

    # Send to API
    response = client.get("/registrations")
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    # there should only be one registration in the list
    assert len(response_json) == 1


def test_delete_registration():
    ###
    # DELETE /favourites/<id>
    ##

    # Send to API
    response = client.delete(
        "/registrations/"+str(registration["id"]), content_type="application/json")

    # Check response
    assert response.status_code == 200


def test_delete_relations():
    ###
    # This deletes the test relations we set up, so they don't
    # remain in the db
    ###
    dancer_response = client.delete(
        "/dancers/"+str(dancer["id"]), content_type="application/json")
    event_response = client.delete(
        "/events/"+str(event["id"]), content_type="application/json")
    studio_response = client.delete(
        "/studios/"+str(studio["id"]), content_type="application/json")

    # Check that the deletes were successful
    assert dancer_response.status_code == 200
    assert event_response.status_code == 200
    assert studio_response.status_code == 200
