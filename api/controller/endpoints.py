from flask import Flask, request
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir)
from services.account import *
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