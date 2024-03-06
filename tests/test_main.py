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


def test_index_successful(client):
    response = client.get("/")
    assert b"""<h1 class="title">
    Simple Summary Site
</h1>
<h2 class="subtitle">
    Summarise your items and costs.
</h2>""" in response.data

