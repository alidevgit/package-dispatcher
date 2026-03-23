from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


VOLUME_THRESHOLD_CM3 = 1_000_000
DIMENSION_THRESHOLD_CM = 150
MASS_THRESHOLD_KG = 20


class Stack(StrEnum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"


@dataclass(frozen=True, slots=True)
class Package:
    width: float
    height: float
    length: float
    mass: float

    def __post_init__(self) -> None:
        for name, value in (
            ("width", self.width),
            ("height", self.height),
            ("length", self.length),
            ("mass", self.mass),
        ):
            if value < 0:
                raise ValueError(f"{name} must be non-negative")

    @property
    def volume(self) -> float:
        return self.width * self.height * self.length

    @property
    def is_bulky(self) -> bool:
        return (
            self.volume >= VOLUME_THRESHOLD_CM3
            or self.width >= DIMENSION_THRESHOLD_CM
            or self.height >= DIMENSION_THRESHOLD_CM
            or self.length >= DIMENSION_THRESHOLD_CM
        )

    @property
    def is_heavy(self) -> bool:
        return self.mass >= MASS_THRESHOLD_KG


def sort(width: float, height: float, length: float, mass: float) -> str:
    package = Package(width=width, height=height, length=length, mass=mass)

    if package.is_bulky and package.is_heavy:
        return Stack.REJECTED
    if package.is_bulky or package.is_heavy:
        return Stack.SPECIAL
    return Stack.STANDARD
