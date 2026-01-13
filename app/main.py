from __future__ import annotations


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        elif isinstance(other, (int, float)):
            return Distance(
                km=self.km + other
            )
        else:
            raise TypeError(f"unexpected type for {type(other)}")

    def __iadd__(self, other: Distance | float | int) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(f"Unsupported operand type(s) "
                            f"for +=: {type(other)}")
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(
                km=self.km * other
            )
        else:
            raise TypeError(f"Unsupported operand type(s) "
                            f"for +=: {type(other)}")

    def __truediv__(self, other: int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError(
                f"unsupported operand type(s) for /: "
                f"'Distance' and '{type(other).__name__}'"
            )

        km = self.km / other
        return Distance(round(km, 2))

    def __lt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            lt = self.km < other.km
        else:
            lt = self.km < other
        return lt

    def __le__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            le = self.km <= other.km
        else:
            le = self.km <= other
        return le

    def __eq__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            eq = self.km == other.km
        else:
            eq = self.km == other
        return eq

    def __ge__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            ge = self.km >= other.km
        else:
            ge = self.km >= other
        return ge

    def __gt__(self, other: Distance | float | int) -> bool:
        if isinstance(other, Distance):
            gt = self.km > other.km
        else:
            gt = self.km > other
        return gt
