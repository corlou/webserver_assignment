import json
from .app import create_test_client

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


def test_create_studio():
    ###
    # POST /studios
    ##

    # Send to API
    response = client.post(
        "/studios", content_type="application/json", json=studio)
    response_json = json.loads(response.data.decode("utf-8"))
    studio["id"] = response_json["id"]  # save this for our other tests

    # Check response
    assert response.status_code == 200
    assert response_json["id"] != None
    assert response_json['name'] == studio["name"]


def test_update_studio():
    ###
    # PUT /studios/<id>
    ##

    # Prepare studio changes
    studio["name"] = "changed name"
    studio["street_name"] = "changed name"

    # Send to API
    response = client.put(
        "/studios/"+str(studio["id"]), content_type="application/json", json=studio)
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    assert response_json['name'] == studio["name"]
    assert response_json['street_name'] == studio["street_name"]


def test_get_studio():
    ###
    # GET /studios/<id>
    ##

    # Send to API
    response = client.get(
        "/studios/"+str(studio["id"]), content_type="application/json")
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    assert response_json["id"] == studio["id"]


def test_list_studios():
    ###
    # GET /studios
    ##

    # Send to API
    response = client.get("/studios")
    print(response.data.decode("utf-8"))
    response_json = json.loads(response.data.decode("utf-8"))

    # Check response
    assert response.status_code == 200
    # there should only be one studio in the list
    assert len(response_json) == 1


def test_delete_studio():
    ###
    # DELETE /studios/<id>
    ##

    # Send to API
    response = client.delete(
        "/studios/"+str(studio["id"]), content_type="application/json")

    # Check response
    assert response.status_code == 200
