
def setup_module(module):
    print("creating a DB connection")
def teardown_module(module):
    print("closing DB connection")

def setup_function(function):
    print("launching Browser")


def teardown_function(function):
    print("quit the browser")


def test_doLogin():
    print("executing login test")


def test_regis():
    print("executing user resign")
