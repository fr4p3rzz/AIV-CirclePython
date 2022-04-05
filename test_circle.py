import pytest
import numpy as np
from circle import Circle


@pytest.fixture
def circles():
    circles = [Circle(True, 8), Circle(False, 8), Circle(True, 8)]
    return circles

def test_circle__init__(mocker):
    mocker.patch("uuid.uuid4", return_value = "1")
    circle_test = Circle(True, 8)
    assert circle_test._radius == 8
    assert circle_test._diameter == 16
    assert circle_test._id == "1"

def test__add__(circles):
    assert circles[0] + circles[1] == Circle(True, 12)

def test__lt__(circles):
    assert circles[1] < circles[0]

def test__gt__(circles):
    assert circles[0] > circles[1]

def test__eq__(circles):
    assert circles[0] == circles[2]

def test_area(circles):
    assert circles[0].area() == np.pi * (8 ** 2)
    assert circles[1].area() == np.pi * (4 ** 2)
    assert circles[2].area() == np.pi * (8 ** 2)

def test_compare_dimension(mocker):
    mocker.patch("uuid.uuid4", return_value = "1")
    circle_1 = Circle(True, 4)
    circle_2 = Circle(True, 8)
    circle_3 = Circle(True, 8)
    assert circle_2.compare_dimension(circle_1) == f"Circle 1 is bigger than circle 1."
    assert circle_1.compare_dimension(circle_2) == f"Circle 1 is smaller than circle 1."
    assert circle_2.compare_dimension(circle_3) == f"Circles are equal"

def test_show_circle(circles):
    theta = np.linspace(0, 2*np.pi, 100)
    a = circles[0]._radius*np.cos(theta)
    b = circles[0]._radius*np.sin(theta)
    for x in a:
        assert x >= -circles[0]._radius and x <= circles[0]._radius
    for x in b:
        assert x >= -circles[0]._radius and x <= circles[0]._radius
