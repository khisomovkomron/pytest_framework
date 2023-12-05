import pytest


def pytest_addoption(parser):
    parser.addoption("--env", help="Which of envs must start")


@pytest.fixture(scope="function")
def env(request):
    return request.config.getoption("env")
