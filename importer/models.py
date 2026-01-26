from dataclasses import dataclass


@dataclass(frozen=True)
class SpecificationPart:
    drawing_number: str
    name: str
    width: float
    height: float
    quantity: int
    material_id: int