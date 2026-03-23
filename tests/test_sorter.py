import pytest

from package_dispatcher import sort


@pytest.mark.parametrize(
    ("width", "height", "length", "mass", "expected"),
    [
        (10, 10, 10, 1, "STANDARD"),
        (150, 10, 10, 1, "SPECIAL"),
        (149.9, 10, 10, 1, "STANDARD"),
        (100, 100, 100, 1, "SPECIAL"),
        (100, 100, 99.99, 1, "STANDARD"),
        (10, 10, 10, 20, "SPECIAL"),
        (10, 10, 10, 19.99, "STANDARD"),
        (150, 10, 10, 20, "REJECTED"),
        (100, 100, 100, 20, "REJECTED"),
        (200, 200, 200, 100, "REJECTED"),
    ],
)
def test_sort(width: float, height: float, length: float, mass: float, expected: str) -> None:
    assert sort(width, height, length, mass) == expected


@pytest.mark.parametrize("bad_value", [-0.01, -1])
def test_negative_inputs_raise_value_error(bad_value: float) -> None:
    with pytest.raises(ValueError):
        sort(bad_value, 1, 1, 1)

    with pytest.raises(ValueError):
        sort(1, bad_value, 1, 1)

    with pytest.raises(ValueError):
        sort(1, 1, bad_value, 1)

    with pytest.raises(ValueError):
        sort(1, 1, 1, bad_value)
