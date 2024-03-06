import pytest

import summary_site


@pytest.fixture()
def app():
    app = summary_site.create_app()
    app.config.update({
        "TESTING": True,
        "LOGIN_DISABLED": True
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_summary_successful():
    pass


def test_empty_summary_handled():
    pass
