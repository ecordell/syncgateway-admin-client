import requests
import requests_mock

from . import conftest as fixtures


def mock_session():
    session = requests.Session()
    adapter = requests_mock.Adapter()
    session.mount(fixtures.url(), adapter)
    add_session_endpoint(adapter)
    add_user_endpoint(adapter)
    add_role_endpoint(adapter)
    return session


def add_session_endpoint(adapter):
    get_body = {
        "authentication_handlers": ["default", "cookie"],
        "ok": True,
        "userCtx": {
            "channels": {},
            "name": "chef123"
        }
    }
    adapter.register_uri(
        'GET',
        fixtures.database_url() + '/_session/' + fixtures.good_session_id(),
        json=get_body,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )
    adapter.register_uri(
        'GET',
        fixtures.database_url() + '/_session/' + fixtures.bad_session_id(),
        status_code=404,
        headers={'Content-Type': 'application/json'}
    )

    post_body = {
        "cookie_name": "SyncGatewaySession",
        "expires": "2014-11-07T16:42:11.675519255-08:00",
        "session_id": "c2425fa7d734bc8c3f6c507854166bef56a5fbc6"
    }
    adapter.register_uri(
        'POST',
        fixtures.database_url() + '/_session',
        status_code=200,
        json=post_body,
        headers={'Content-Type': 'application/json'}
    )

    adapter.register_uri(
        'DELETE',
        fixtures.database_url() + '/_session/' + fixtures.good_session_id(),
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )
    adapter.register_uri(
        'DELETE',
        fixtures.database_url() + '/_session/' + fixtures.bad_session_id(),
        status_code=404,
        headers={'Content-Type': 'application/json'}
    )
    adapter.register_uri(
        'DELETE',
        (fixtures.database_url() + '/_user/' +
         fixtures.good_username() + '/_session'),
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )


def add_user_endpoint(adapter):
    list_body = ["chef123", "zack", "adam", "pasin"]
    adapter.register_uri(
        'GET',
        fixtures.database_url() + '/_user',
        json=list_body,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )

    user_body = {
        "name": "chef123",
        "admin_channels": ["admin_events"],
        "all_channels": ["!", "events", "admin_events"]
    }
    adapter.register_uri(
        'GET',
        fixtures.database_url() + '/_user/' + fixtures.good_username(),
        json=user_body,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )
    adapter.register_uri(
        'GET',
        fixtures.database_url() + '/_user/' + fixtures.bad_username(),
        status_code=404,
        headers={'Content-Type': 'application/json'}
    )

    adapter.register_uri(
        'POST',
        fixtures.database_url() + '/_user',
        status_code=201,
        headers={'Content-Type': 'application/json'}
    )

    adapter.register_uri(
        'PUT',
        fixtures.database_url() + '/_user/' + fixtures.good_username(),
        json=user_body,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )

    adapter.register_uri(
        'DELETE',
        fixtures.database_url() + '/_user/' + fixtures.good_username(),
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )


def add_role_endpoint(adapter):
    list_body = ["moderator", "chef", "san francisco"]
    adapter.register_uri(
        'GET',
        fixtures.database_url() + '/_role',
        json=list_body,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )

    role_body = {
        "name": "moderator",
        "all_channels": ["!", "recipes-in-progress"]
    }
    adapter.register_uri(
        'GET',
        fixtures.database_url() + '/_role/' + fixtures.good_role(),
        json=role_body,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )
    adapter.register_uri(
        'GET',
        fixtures.database_url() + '/_role/' + fixtures.bad_role(),
        status_code=404,
        headers={'Content-Type': 'application/json'}
    )

    adapter.register_uri(
        'POST',
        fixtures.database_url() + '/_role',
        status_code=201,
        headers={'Content-Type': 'application/json'}
    )

    adapter.register_uri(
        'PUT',
        fixtures.database_url() + '/_role/' + fixtures.good_role(),
        json=role_body,
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )

    adapter.register_uri(
        'DELETE',
        fixtures.database_url() + '/_role/' + fixtures.good_role(),
        status_code=200,
        headers={'Content-Type': 'application/json'}
    )
