from flask import Flask, request
import sys
import os
from flask import jsonify

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)
from account_app import *
from car_app import *
app = Flask(__name__)

# Account
@app.post("/register")
def handle_register():
    info = request.json
    return jsonify(generate_customer(info))

@app.post("/login")
def handle_login():
    info = request.json
    return jsonify(challenge_password(info))

@app.patch("/edit_profile/<user_id>")
def handle_edit_profile(user_id):
    info = request.json
    return jsonify(edit_profile(info, user_id))

@app.patch("/edit_password")
def handle_edit_password():
    info = request.json
    return jsonify(edit_password_app(info))

@app.patch("/forgot_password")
def handle_forgot_password():
    info = request.json
    return jsonify(forgot_password_app(info.get("email")))

# will do last
@app.delete("/delete_profile/<user_id>")
def handle_delete_profile(user_id):
    return None

@app.get("/profile/cars/<user_id>")
def handle_show_owned_cars(user_id):
    return jsonify(get_owned_cars_app(user_id))

@app.post("/profile/<user_id>/add/cars")
def handle_add_owned_car(user_id):
    return None

# Vehicles
@app.get("/display/cars")
def handle_diplay_cars():
    return jsonify(display_all_cars_app())

if __name__ == '__main__':
    app.run(debug=True, port=8000)