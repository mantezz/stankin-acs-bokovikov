"""Проверка синтаксиса IPv4-адресов."""

from ipaddress import AddressValueError, IPv4Address


def is_valid_ipv4(address: str) -> bool:
    """Проверяет IPv4 в формате четырёх десятичных чисел от 0 до 255.

    Пробелы, ведущие нули, маски подсети и IPv6 не допускаются.
    Проверяется только синтаксис, а не доступность адреса в сети.
    Для значений, которые не являются строками, возвращается False.

    Examples:
        >>> is_valid_ipv4("192.168.1.1")
        True
        >>> is_valid_ipv4("256.168.1.1")
        False
    """
    if not isinstance(address, str):
        return False
    try:
        IPv4Address(address)
    except AddressValueError:
        return False
    return True
