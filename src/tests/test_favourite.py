# import json
# from datetime import datetime
# from .app import create_test_client

# client = create_test_client()

# # A fake favourite we will use to test with
# favourite = {
#     "id": None,  # this will be set when we create a favourite
#     "dancer": "zoe",
#     "event": "tricks"
# }


# def test_create_favourite():
#     ###
#     # POST /favourites
#     ##

#     # Send to API
#     response = client.post(
#         "/favourites", content_type="application/json", json=favourite)
#     response_json = json.loads(response.data.decode("utf-8"))
#     # save this for our other tests
#     favourite["id"] = response_json["id"]

#     # Check response
#     assert response.status_code == 200
#     assert response_json["id"] != None
#     assert response_json['dancer'] == favourite["dancer"]


# def test_update_favourite():
#     ###
#     # PUT /favourites/<id>
#     ##

#     # Prepare favourite changes
#     favourite["dancer"] = "added favourite"
#     favourite["event"] = "event added to favourites"

#     # Send to API
#     response = client.put(
#         "/favourites/"+str(favourite["id"]), content_type="application/json", json=favourite)
#     response_json = json.loads(response.data.decode("utf-8"))

#     # Check response
#     assert response.status_code == 200
#     assert response_json['dancer'] == favourite["dancer"]
#     assert response_json['event'] == favourite["event"]


# def test_get_favourite():
#     ###
#     # GET /favourites/<id>
#     ##

#     # Send to API
#     response = client.get(
#         "/favourites/"+str(favourite["id"]), content_type="application/json")
#     response_json = json.loads(response.data.decode("utf-8"))

#     # Check response
#     assert response.status_code == 200
#     assert response_json["id"] == favourite["id"]


# def test_list_favourites():
#     ###
#     # GET /favourites
#     ##

#     # Send to API
#     response = client.get("/favourites")
#     print(response.data.decode("utf-8"))
#     response_json = json.loads(response.data.decode("utf-8"))

#     # Check response
#     assert response.status_code == 200
#     # there should only be one favourite in the list
#     assert len(response_json) == 1


# def test_delete_favourite():
#     ###
#     # DELETE /favourites/<id>
#     ##

#     # Send to API
#     response = client.delete(
#         "/favourites/"+str(favourite["id"]), content_type="application/json")

#     # Check response
#     assert response.status_code == 200
