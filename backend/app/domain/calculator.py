from dataclasses import dataclass

from app.domain.part import Part
from app.domain.sheet import Sheet


@dataclass(frozen=True)
class AreaResult:
    sheet_area: float
    parts_area: float
    waste_area: float
    utilization: float


class Calculator:
    def calculate_parts_area(
        self,
        parts: list[Part],
    ) -> float:
        return sum(
            part.total_area
            for part in parts
        )

    def calculate_waste_area(
        self,
        sheet: Sheet,
        parts: list[Part],
    ) -> float:
        parts_area = self.calculate_parts_area(parts)

        waste_area = sheet.area - parts_area

        return max(waste_area, 0.0)

    def calculate_utilization(
        self,
        sheet: Sheet,
        parts: list[Part],
    ) -> float:
        if sheet.area == 0:
            return 0.0

        parts_area = self.calculate_parts_area(parts)

        utilization = (
            parts_area / sheet.area
        ) * 100

        return min(utilization, 100.0)

    def calculate(
        self,
        sheet: Sheet,
        parts: list[Part],
    ) -> AreaResult:
        sheet_area = sheet.area
        parts_area = self.calculate_parts_area(parts)

        waste_area = max(
            sheet_area - parts_area,
            0.0,
        )

        utilization = (
            min(
                parts_area / sheet_area * 100,
                100.0,
            )
            if sheet_area > 0
            else 0.0
        )

        return AreaResult(
            sheet_area=sheet_area,
            parts_area=parts_area,
            waste_area=waste_area,
            utilization=utilization,
        )