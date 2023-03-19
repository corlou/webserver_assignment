# import json
# from .app import create_test_client

# client = create_test_client()

# # A fake registration we will use to test with
# registration = {
#     "id": None,  # this will be set when we create a registration
#     "dancer_id": 123,
#     "event_id": 456,
#     "date_registered": "zoe@example.com"
# }


# def test_create_registration():
#     ###
#     # POST /registrations
#     ##

#     # Send to API
#     response = client.post(
#         "/registrations", content_type="application/json", json=registration)
#     response_json = json.loads(response.data.decode("utf-8"))
#     registration["id"] = response_json["id"]  # save this for our other tests

#     # Check response
#     assert response.status_code == 200
#     assert response_json["id"] != None
#     assert response_json['dancer_id'] == registration["dancer_id"]


# def test_update_registration():
#     ###
#     # PUT /registrations/<id>
#     ##

#     # Prepare registration changes
#     registration["dancer_id"] = "changed name"
#     registration["event_id"] = "changed email"

#     # Send to API
#     response = client.put(
#         "/registrations/"+str(registration["id"]), content_type="application/json", json=registration)
#     response_json = json.loads(response.data.decode("utf-8"))

#     # Check response
#     assert response.status_code == 200
#     assert response_json['name'] == registration["name"]
#     assert response_json['email'] == registration["email"]


# def test_get_registration():
#     ###
#     # GET /retistrations/<id>
#     ##

#     # Send to API
#     response = client.get(
#         "/registrations/"+str(registration["id"]), content_type="application/json")
#     response_json = json.loads(response.data.decode("utf-8"))

#     # Check response
#     assert response.status_code == 200
#     assert response_json["id"] == registration["id"]


# def test_list_registrations():
#     ###
#     # GET /registrations
#     ##

#     # Send to API
#     response = client.get("/registrations")
#     print(response.data.decode("utf-8"))
#     response_json = json.loads(response.data.decode("utf-8"))

#     # Check response
#     assert response.status_code == 200
#     # there should only be one registration in the list
#     assert len(response_json) == 1


# def test_delete_registration():
#     ###
#     # DELETE /registrations/<id>
#     ##

#     # Send to API
#     response = client.delete(
#         "/registrations/"+str(registration["id"]), content_type="application/json")

#     # Check response
#     assert response.status_code == 200
