from dataclasses import dataclass

from app.domain.part import Part


@dataclass(frozen=True)
class Placement:
    part: Part
    x: float
    y: float
    width: float
    height: float
    rotated: bool = False

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def right(self) -> float:
        return self.x + self.width

    @property
    def top(self) -> float:
        return self.y + self.height