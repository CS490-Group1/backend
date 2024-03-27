from conftest import client

def test_register_success():
    response = client.post("/register", json={
        "email":"something@gmail.com",
        "first_name":"Hello",
        "last_name":"World",
        "dob":"",
        "drivers_license":"",
        "phone":"",
        "password":"password123",
    })