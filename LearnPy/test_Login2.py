import pytest


def test_login1():
    print("This is login test1")


def test_add_item1():
    print("Item Added to Cart1")


@pytest.mark.smoke
def test_logout1():
    print("User cd logged out1")
