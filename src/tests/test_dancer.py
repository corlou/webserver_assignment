import json
from .app import create_test_client

client = create_test_client()

# A fake dancer we will use to test with
dancer = {
    "id": None,  # this will be set when we create a dancer
    "name": "zoe",
    "password": "password",
    "email": "zoe@example.com",
    "date_of_birth": "1990-01-01",
    "studio_id": None,
}

# A fake studio we will use to test with
studio = {
    "id": None,  # this will be set when we create a studio
    "name": "Csolta",
    "street_num": "123",
    "street_name": "Moggill Road",
    "postcode": 4068,
    "contact_num": "0411222333",
}


def test_create_relations():
    ###
    # This sets up the db with the relations we need to test
    # the favourites
    ###
    # Studio
    studio_response = client.post(
        "/studios", content_type="application/json", json=studio)
    studio_response_json = json.loads(studio_response.data.decode("utf-8"))
    # Populate the test entities
    studio["id"] = studio_response_json["id"]
    dancer["studio_id"] = studio["id"]
    # Check that our test records got created
    assert studio_response.status_code == 200


def test_create_dancer():
    ###
    # POST /dancers
    ##

    # Send to API
    response = client.post(
        "/dancers", content_type="application/json", json=dancer)
    response_json = json.loads(response.data.decode("utf-8"))
    dancer["id"] = response_json["id"]  # save this for our other tests

    # Check response
    assert response.status_code == 200
    assert response_json["id"] != None
    assert response_json['name'] == dancer["name"]


def test_update_dancer():
    ###
    # PUT /dancers/<id>
    ##

    # Prepare dancer changes
    dancer["name"] = "changed name"
    dancer["email"] = "changed email"

    # Send to API
    response = client.put(
        "/dancers/"+str(dancer["id"]), content_type="application/json", json=dancer)
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    assert response_json['name'] == dancer["name"]
    assert response_json['email'] == dancer["email"]


def test_get_dancer():
    ###
    # GET /dancers/<id>
    ##

    # Send to API
    response = client.get(
        "/dancers/"+str(dancer["id"]), content_type="application/json")
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    assert response_json["id"] == dancer["id"]


def test_list_dancers():
    ###
    # GET /dancers
    ##

    # Send to API
    response = client.get("/dancers")
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    # there should only be one dancer in the list
    assert len(response_json) == 1


def test_delete_dancer():
    ###
    # DELETE /dancers/<id>
    ##

    # Send to API
    response = client.delete(
        "/dancers/"+str(dancer["id"]), content_type="application/json")

    # Check response
    assert response.status_code == 200


def test_delete_relations():
    ###
    # This deletes the test relations we set up, so they don't
    # remain in the db
    ###
    studio_response = client.delete(
        "/studios/"+str(studio["id"]), content_type="application/json")

    # Check that the deletes were successful
    assert studio_response.status_code == 200
