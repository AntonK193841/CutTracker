from app.domain.nesting import NestingCalculator
from app.domain.part import Part
from app.domain.sheet import Sheet


def test_parts_are_placed_on_sheet():
    calculator = NestingCalculator()

    sheet = Sheet(
        width=1000,
        height=1000,
    )

    parts = [
        Part(
            name="A",
            width=200,
            height=200,
            quantity=2,
        ),
    ]

    result = calculator.calculate(
        sheet,
        parts,
    )

    assert len(result.placements) == 2
    assert len(result.unplaced_parts) == 0


def test_part_coordinates_are_inside_sheet():
    calculator = NestingCalculator()

    sheet = Sheet(
        width=1000,
        height=1000,
    )

    parts = [
        Part(
            name="A",
            width=400,
            height=300,
            quantity=3,
        ),
    ]

    result = calculator.calculate(
        sheet,
        parts,
    )

    for placement in result.placements:
        assert placement.x >= 0
        assert placement.y >= 0
        assert placement.right <= sheet.width
        assert placement.top <= sheet.height


def test_part_can_be_rotated():
    calculator = NestingCalculator()

    sheet = Sheet(
        width=500,
        height=300,
    )

    parts = [
        Part(
            name="A",
            width=300,
            height=500,
        ),
    ]

    result = calculator.calculate(
        sheet,
        parts,
    )

    assert len(result.placements) == 1
    assert result.placements[0].rotated is True


def test_unplaced_part_is_reported():
    calculator = NestingCalculator()

    sheet = Sheet(
        width=100,
        height=100,
    )

    parts = [
        Part(
            name="Too Large",
            width=200,
            height=200,
        ),
    ]

    result = calculator.calculate(
        sheet,
        parts,
    )

    assert len(result.placements) == 0
    assert len(result.unplaced_parts) == 1


def test_nesting_calculates_utilization():
    calculator = NestingCalculator()

    sheet = Sheet(
        width=1000,
        height=1000,
    )

    parts = [
        Part(
            name="A",
            width=500,
            height=500,
            quantity=2,
        ),
    ]

    result = calculator.calculate(
        sheet,
        parts,
    )

    assert result.placed_area == 500_000
    assert result.waste_area == 500_000
    assert result.utilization == 50