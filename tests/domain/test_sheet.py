import pytest

from app.domain.part import Part
from app.domain.sheet import Sheet


def test_sheet_area():
    sheet = Sheet(
        width=2000,
        height=1000,
    )

    assert sheet.area == 2_000_000


def test_part_fits_on_sheet():
    sheet = Sheet(
        width=2000,
        height=1000,
    )

    part = Part(
        name="Part",
        width=500,
        height=300,
    )

    assert sheet.can_fit(part)


def test_part_does_not_fit_on_sheet():
    sheet = Sheet(
        width=1000,
        height=500,
    )

    part = Part(
        name="Part",
        width=1200,
        height=300,
    )

    assert not sheet.can_fit(part)


def test_part_fits_after_rotation():
    sheet = Sheet(
        width=1000,
        height=500,
    )

    part = Part(
        name="Part",
        width=300,
        height=1200,
    )

    assert sheet.can_fit_rotated(part)
    assert sheet.can_fit_with_rotation(part)


def test_sheet_rejects_invalid_dimensions():
    with pytest.raises(ValueError):
        Sheet(
            width=0,
            height=1000,
        )