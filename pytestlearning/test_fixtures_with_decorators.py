import pytest


@pytest.fixture(scope='module')
def setup():
    print("creating a DB connection")

    yield
    print("closing DB connection")


@pytest.fixture(scope='function')
def before():
    print("Launching browser")
    yield
    print("closing browser")


# def test_dologin(setup,before):
#     print("executing login test")
#
#
# def test_regis(setup,before):
#     print("executing user resign")

@pytest.mark.usefixtures("setup", "before")
def test_dologin():
    print("executing login test")


@pytest.mark.usefixtures("setup", "before")
def test_regis():
    print("executing user resign")
