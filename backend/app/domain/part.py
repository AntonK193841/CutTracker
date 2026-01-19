from dataclasses import dataclass


@dataclass(frozen=True)
class Part:
    name: str
    width: float
    height: float
    quantity: int = 1

    def __post_init__(self):
        if self.width <= 0:
            raise ValueError("Part width must be greater than zero")

        if self.height <= 0:
            raise ValueError("Part height must be greater than zero")

        if self.quantity <= 0:
            raise ValueError("Part quantity must be greater than zero")

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def total_area(self) -> float:
        return self.area * self.quantity

    def rotated(self) -> "Part":
        return Part(
            name=self.name,
            width=self.height,
            height=self.width,
            quantity=self.quantity,
        )