import pytest


def test_login():
    print("This is login test")

@pytest.mark.smoke
def test_add_item():
    print("Item Added to Cart")

@pytest.mark.skip
def test_logout():
    print("User cd logged out")