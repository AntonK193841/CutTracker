from app.domain.calculator import Calculator
from app.domain.part import Part
from app.domain.sheet import Sheet


def test_calculate_parts_area():
    calculator = Calculator()

    parts = [
        Part(
            name="Part 1",
            width=100,
            height=100,
            quantity=2,
        ),
        Part(
            name="Part 2",
            width=200,
            height=100,
            quantity=1,
        ),
    ]

    result = calculator.calculate_parts_area(parts)

    assert result == 40_000


def test_calculate_waste_area():
    calculator = Calculator()

    sheet = Sheet(
        width=1000,
        height=1000,
    )

    parts = [
        Part(
            name="Part",
            width=500,
            height=500,
        ),
    ]

    result = calculator.calculate_waste_area(
        sheet,
        parts,
    )

    assert result == 750_000


def test_calculate_utilization():
    calculator = Calculator()

    sheet = Sheet(
        width=1000,
        height=1000,
    )

    parts = [
        Part(
            name="Part",
            width=500,
            height=500,
        ),
    ]

    result = calculator.calculate_utilization(
        sheet,
        parts,
    )

    assert result == 25


def test_calculate():
    calculator = Calculator()

    sheet = Sheet(
        width=1000,
        height=1000,
    )

    parts = [
        Part(
            name="Part",
            width=500,
            height=500,
            quantity=2,
        ),
    ]

    result = calculator.calculate(
        sheet,
        parts,
    )

    assert result.sheet_area == 1_000_000
    assert result.parts_area == 500_000
    assert result.waste_area == 500_000
    assert result.utilization == 50