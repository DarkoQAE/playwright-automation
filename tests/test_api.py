import requests

BASE_URL = "https://reqres.in/api/users"  # Public API for testing

def test_get_users():
    """ Test GET request to fetch users """
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_user():
    """ Test POST request to create a user """
    payload = {
        "name": "Darko",
        "job": "QA Engineer"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201  # 201 Created
    assert response.json()["name"] == "Darko"

def test_update_user():
    """ Test PUT request to update a user """
    user_id = 2  # Update user with ID 2
    payload = {
        "name": "Darko Updated",
        "job": "Automation QA"
    }
    response = requests.put(f"{BASE_URL}/{user_id}", json=payload)
    assert response.status_code == 200  # 200 OK
    assert response.json()["name"] == "Darko Updated"

def test_delete_user():
    """ Test DELETE request to remove a user """
    user_id = 2  # Deleting user with ID 2
    response = requests.delete(f"{BASE_URL}/{user_id}")
    assert response.status_code == 204  # 204 No Content