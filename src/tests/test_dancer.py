import json
from src.app import create_app

# Allows us to test our routes
client = create_app().test_client()

# A fake dancer we will use to test with
dancer = {
    "id": None,  # this will be set when we create a dancer
    "name": "zoe",
    "password": "password",
    "email": "zoe@example.com",
    "date_of_birth": "1990-01-01"
}


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
    print(response.data.decode("utf-8"))
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