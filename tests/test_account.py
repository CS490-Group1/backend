from tests.conftest import client

def test_register_success(client):
    response = client.post("/register", json={
        "email":"creamsicle@gmail.com",
        "first_name":"Bye",
        "last_name":"Chat",
        "dob":"01/02/2000",
        "drivers_license":"AB120312321",
        "phone":"1023912310",
        "password":"password123",
    })
    assert response.json['status'] == 'success'

def test_register_fail(client):
    response = client.post("/register", json={
        "email":"creamsicle@gmail.com",
        "first_name":"Bye",
        "last_name":"Chat",
        "dob":"01/02/2000",
        "drivers_license":"AB120312321",
        "phone":"1023912310",
        "password":"password123",
    })
    assert response.json['status'] == 'fail'

def test_authentication_success(client):
    response = client.post("/login", json={
        "email":"creamsicle@gmail.com",
        "password":"password123"
    })
    assert response.json['status'] == 'success'

def test_authentication_success(client):
    response = client.post("/login", json={
        "email":"creamsicle@gmail.com",
        "password":"password1234"
    })
    assert response.json['status'] == 'fail'

def test_drivers_license_valid(client):
    response = client.patch("/edit_profile/31", json={
        "phone":"12310239123",
        "dob":"12/14/1999",
        "first_name":"Hi",
        "drivers_license":"thisisfakedriverslicense"
    })
    assert response.json['status'] == 'fail'

def test_edit_success(client):
    response = client.patch("/edit_profile/31", json={
        "phone":"12310239123",
        "dob":"12/14/1999",
        "first_name":"Hi",
        "drivers_license":"Y102312021"
    })
    assert response.json['status'] == 'success'

def test_forget_password(client):
    response = client.patch("/forgot_password", json={
        "email":"creamsicle@gmail.com"
    })
    assert response.json['status'] == 'success'
    new_password = response.json['new_password']

    response = client.patch("/edit_password", json={
        "email":"creamsicle@gmail.com",
        "password":new_password,
        "new_password":"icecreamsogood12"
    })

def test_get_owned_cars(client):
    response = client.get("/profile/cars/31")
    assert response.status_code == 200