import pytest


#@pytest.fixture(autouse=True,scope="session")  # to only once per session
#@pytest.fixture(autouse=True,scope="class")   # to run at class level
#@pytest.fixture(autouse=True,scope="function")  # to run at each test present in the test file
#@pytest.fixture(autouse=True,scope="module")   # to run per module
@pytest.fixture(autouse=True, scope="package")  # to run per package
def setup_tear_down():
    print("I will run before every test")
    print("launched the browser")
    yield
    print("I will run after every test")
    print("closed the browser")
