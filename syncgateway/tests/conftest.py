import pytest

from syncgateway.client import Client
from . import mock_session


@pytest.fixture(scope="module")
def client():
    return Client(admin_url=url(), database=database_name(), session=request_session())


@pytest.fixture(scope="module")
def request_session():
    return mock_session.mock_session() 


@pytest.fixture(scope="module")
def database_name():
    return "db"


@pytest.fixture(scope="module")
def url():
    return "http://cb-admin.com"


@pytest.fixture(scope="module")
def database_url():
    return url() + '/' + database_name()


@pytest.fixture(scope="module")
def good_session_id():
    return "sess_id"


@pytest.fixture(scope="module")
def bad_session_id():
    return "bad_sess_id"


@pytest.fixture(scope="module")
def good_username():
    return "user"


@pytest.fixture(scope="module")
def bad_username():
    return "bad_user"


@pytest.fixture(scope="module")
def good_role():
    return "role"


@pytest.fixture(scope="module")
def bad_role():
    return "bad_role"
