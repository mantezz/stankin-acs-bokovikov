import pytest

from ipv4_validator import is_valid_ipv4


def test_all_valid_fixture_addresses(valid_ipv4_addresses):
    for address in valid_ipv4_addresses:
        assert is_valid_ipv4(address) is True, f"Должен быть корректным: {address!r}"


def test_all_invalid_fixture_addresses(invalid_ipv4_addresses):
    for address in invalid_ipv4_addresses:
        assert is_valid_ipv4(address) is False, f"Должен быть некорректным: {address!r}"


@pytest.mark.parametrize("value", [None, 0, 3232235777, True, b"192.168.1.1", [], {}, [192, 168, 1, 1]])
def test_non_string_values(value):
    assert is_valid_ipv4(value) is False


@pytest.mark.parametrize("position", range(4))
@pytest.mark.parametrize("value, expected", [(0, True), (1, True), (254, True), (255, True), (256, False), (-1, False)])
def test_octet_boundaries(position, value, expected):
    octets = ["1", "2", "3", "4"]
    octets[position] = str(value)
    assert is_valid_ipv4(".".join(octets)) is expected
