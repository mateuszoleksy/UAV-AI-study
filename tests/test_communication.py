"""Basic tests for the communication module."""

from src.communication.link_model import LinkParameters


def test_free_space_path_loss_positive():
    link = LinkParameters()
    loss = link.free_space_path_loss_db(100.0)
    assert loss > 0


def test_free_space_path_loss_zero_distance():
    link = LinkParameters()
    assert link.free_space_path_loss_db(0.0) == 0.0


def test_received_power_decreases_with_distance():
    link = LinkParameters()
    p1 = link.received_power_dbm(100.0)
    p2 = link.received_power_dbm(200.0)
    assert p1 > p2


def test_link_viable_short_range():
    link = LinkParameters(tx_power_dbm=30.0, rx_sensitivity_dbm=-90.0)
    assert link.is_link_viable(10.0)


def test_link_not_viable_extreme_range():
    link = LinkParameters(tx_power_dbm=10.0, rx_sensitivity_dbm=-60.0)
    assert not link.is_link_viable(1_000_000.0)
