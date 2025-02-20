import pytest
import requests_mock
from api_client.teamcity_client import TeamCityClient
from utils.data_generator import DataGenerator


@pytest.fixture(scope="session")
def teamcity_client():
    return TeamCityClient()


@pytest.fixture(scope="session")
def data_generator():
    return DataGenerator()


@pytest.fixture
def mock_requests():
    with requests_mock.Mocker() as m:
        yield m
