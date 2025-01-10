import ptest
import pytest


@pytest.mark.smoke
def test_login1():
    print("This is login test2")


def test_add_item1():
    print("Item Added to Cart2")

@pytest.mark.xfail
def test_logout1():
    print("User cd logged out2")