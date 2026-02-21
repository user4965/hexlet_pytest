from pathlib import Path

from hexlet_pytest.example import reverse


def read_test_data(filename: str) -> str:
    return (Path(__file__).parent / "test_data" / filename).read_text()


def test_reverse_with_long_text():
    source = read_test_data("input.txt")
    expected = read_test_data("expected.txt")
    assert reverse(source) == expected