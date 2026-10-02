from src.payment import calculate_total


def test_no_discount():
    assert calculate_total(100, 2) == 200


def test_with_discount():
    assert calculate_total(100, 2, 10) == 180
