from dataclasses import dataclass

from app.domain.part import Part
from app.domain.placement import Placement
from app.domain.sheet import Sheet


@dataclass(frozen=True)
class NestingResult:
    sheet: Sheet
    placements: list[Placement]
    unplaced_parts: list[Part]

    @property
    def placed_area(self) -> float:
        return sum(
            placement.area
            for placement in self.placements
        )

    @property
    def waste_area(self) -> float:
        return max(
            self.sheet.area - self.placed_area,
            0.0,
        )

    @property
    def utilization(self) -> float:
        if self.sheet.area == 0:
            return 0.0

        return (
            self.placed_area / self.sheet.area
        ) * 100


class NestingCalculator:
    def calculate(
        self,
        sheet: Sheet,
        parts: list[Part],
    ) -> NestingResult:
        expanded_parts = self._expand_parts(parts)

        sorted_parts = sorted(
            expanded_parts,
            key=lambda part: max(part.width, part.height),
            reverse=True,
        )

        placements: list[Placement] = []
        unplaced_parts: list[Part] = []

        x = 0.0
        y = 0.0
        row_height = 0.0

        for part in sorted_parts:
            placement = self._find_placement(
                sheet=sheet,
                part=part,
                x=x,
                y=y,
                row_height=row_height,
            )

            if placement is None:
                unplaced_parts.append(part)
                continue

            placements.append(placement)

            x = placement.right
            row_height = max(
                row_height,
                placement.height,
            )

        return NestingResult(
            sheet=sheet,
            placements=placements,
            unplaced_parts=unplaced_parts,
        )

    def _expand_parts(
        self,
        parts: list[Part],
    ) -> list[Part]:
        expanded: list[Part] = []

        for part in parts:
            for _ in range(part.quantity):
                expanded.append(
                    Part(
                        name=part.name,
                        width=part.width,
                        height=part.height,
                    )
                )

        return expanded

    def _find_placement(
        self,
        sheet: Sheet,
        part: Part,
        x: float,
        y: float,
        row_height: float,
    ) -> Placement | None:
        orientations = [
            (
                part.width,
                part.height,
                False,
            ),
            (
                part.height,
                part.width,
                True,
            ),
        ]

        for width, height, rotated in orientations:
            if (
                x + width <= sheet.width
                and y + height <= sheet.height
            ):
                return Placement(
                    part=part,
                    x=x,
                    y=y,
                    width=width,
                    height=height,
                    rotated=rotated,
                )

        if x > 0:
            next_y = y + row_height

            for width, height, rotated in orientations:
                if (
                    width <= sheet.width
                    and next_y + height <= sheet.height
                ):
                    return Placement(
                        part=part,
                        x=0,
                        y=next_y,
                        width=width,
                        height=height,
                        rotated=rotated,
                    )

        return None