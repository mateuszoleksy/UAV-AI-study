"""Basic tests for the navigation module."""

import math

import numpy as np

from src.navigation.path_planning import Path, Waypoint


def test_waypoint_to_array():
    wp = Waypoint(1.0, 2.0, 3.0)
    arr = wp.to_array()
    assert arr.shape == (3,)
    np.testing.assert_array_equal(arr, [1.0, 2.0, 3.0])


def test_path_total_length_empty():
    p = Path()
    assert p.total_length() == 0.0


def test_path_total_length_single():
    p = Path([Waypoint(0.0, 0.0, 0.0)])
    assert p.total_length() == 0.0


def test_path_total_length_two_points():
    p = Path([Waypoint(0.0, 0.0, 0.0), Waypoint(3.0, 4.0, 0.0)])
    assert math.isclose(p.total_length(), 5.0, rel_tol=1e-9)


def test_path_len():
    p = Path([Waypoint(0.0, 0.0, 0.0), Waypoint(1.0, 1.0, 1.0)])
    assert len(p) == 2


def test_path_append():
    p = Path()
    p.append(Waypoint(1.0, 2.0, 3.0))
    assert len(p) == 1
