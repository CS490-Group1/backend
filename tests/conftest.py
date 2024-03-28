import pytest
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../api/controller'))
sys.path.append(parent_dir)
from app import app as my_app

@pytest.fixture()
def app():
    app = my_app
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()