from flask import Flask, request
from backend.services.account import *
import sys
port = 8000
app = Flask(__name__)


@app.post("/register")
def handle_register():
    info = request.json
    customer = create_customer(info)
    return [customer.email, customer.first_name, customer.last_name]

@app.get("/signin")
def handle_signin():
    info = request.json
    customer = grab_customer(info)
    return [customer.email, customer.first_name, customer.last_name]

if __name__ == '__main__':
    app.run(debug=True, port=8000)