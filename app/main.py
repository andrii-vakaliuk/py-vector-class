from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_coor: float, y_coor: float) -> None:
        self.x_coor = round(x_coor, 2)
        self.y_coor = round(y_coor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x_coor + other.x_coor, self.y_coor + other.y_coor)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x_coor - other.x_coor, self.y_coor - other.y_coor)

    def __mul__(
            self, other: Vector | int | float
    ) -> Union[Vector, float, int]:
        if isinstance(other, int | float):
            return Vector(self.x_coor * other, self.y_coor * other)
        return self.x_coor * other.x_coor + self.y_coor * other.y_coor

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        return cls(dx, dy)

    def get_length(self) -> float:
        return (self.x_coor ** 2 + self.y_coor ** 2) ** 0.5

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x_coor, self.y_coor))
        if angle < 0:
            angle = abs(angle)
        return round(angle)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x_coor / length, self.y_coor / length)

    def angle_between(self, other: Vector) -> float:
        dot_pr = ((self.x_coor * other.x_coor) + (self.y_coor * other.y_coor))
        cos_a = dot_pr / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = (self.x_coor * math.cos(radians)
                 - self.y_coor * math.sin(radians))
        new_y = (self.x_coor * math.sin(radians)
                 + self.y_coor * math.cos(radians))
        return Vector(new_x, new_y)
