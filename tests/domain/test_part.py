import pytest

from app.domain.part import Part


def test_part_area():
    part = Part(
        name="Test Part",
        width=100,
        height=50,
    )

    assert part.area == 5000


def test_part_total_area():
    part = Part(
        name="Test Part",
        width=100,
        height=50,
        quantity=4,
    )

    assert part.total_area == 20000


def test_part_rotation():
    part = Part(
        name="Test Part",
        width=100,
        height=50,
    )

    rotated = part.rotated()

    assert rotated.width == 50
    assert rotated.height == 100


def test_part_rejects_invalid_dimensions():
    with pytest.raises(ValueError):
        Part(
            name="Invalid",
            width=0,
            height=100,
        )


def test_part_rejects_invalid_quantity():
    with pytest.raises(ValueError):
        Part(
            name="Invalid",
            width=100,
            height=100,
            quantity=0,
        )