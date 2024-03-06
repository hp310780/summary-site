import pytest
import mock
from flask import current_app

import summary_site
from summary_site.main import get_items_for_user
from summary_site.models import User


@pytest.fixture(scope='session', autouse=True)
def app():
    app = summary_site.create_app()
    app.config.update({
        "TESTING": True,
        "LOGIN_DISABLED": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test_db.sqlite"
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture(scope='session', autouse=True)
def mock_user():
    user = User()
    user.id = 1
    user.name = "Foo"
    user.email = "foo@foo.com"
    user.password = '12345'
    with mock.patch("flask_login.utils._get_user", return_value=user) as _fixture:
        yield _fixture


def test_add_items_successful(client):
    response = client.post("/additem", data={"name": "apples", "price": "10"}, follow_redirects=True)
    assert response.status_code == 200


def test_add_duplicate_item_unsuccessful(client, app):
    pass


def test_db_session_throws_error(client):
    pass
