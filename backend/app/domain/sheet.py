from dataclasses import dataclass

from app.domain.part import Part


@dataclass(frozen=True)
class Sheet:
    width: float
    height: float

    def __post_init__(self):
        if self.width <= 0:
            raise ValueError("Sheet width must be greater than zero")

        if self.height <= 0:
            raise ValueError("Sheet height must be greater than zero")

    @property
    def area(self) -> float:
        return self.width * self.height

    def can_fit(self, part: Part) -> bool:
        return (
            part.width <= self.width
            and part.height <= self.height
        )

    def can_fit_rotated(self, part: Part) -> bool:
        return (
            part.height <= self.width
            and part.width <= self.height
        )

    def can_fit_with_rotation(self, part: Part) -> bool:
        return (
            self.can_fit(part)
            or self.can_fit_rotated(part)
        )