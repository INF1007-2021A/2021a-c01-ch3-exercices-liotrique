#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a ** 2


def average(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degs_to_rad = math.radians(angle_degs)
    mins_to_rad = math.radians(angle_mins / 60)
    secs_to_rad = math.radians(angle_secs / 3600)
    return degs_to_rad + mins_to_rad + secs_to_rad


def to_degrees(angle_rads: float) -> tuple:
    degres_total = math.degrees(angle_rads)
    degres = int(degres_total)
    reste_degres = degres_total - degres

    minutes_total = reste_degres * 60
    minutes = int(minutes_total)
    reste_minutes = minutes_total - minutes

    secondes_total = reste_minutes * 60


    return degres, minutes, secondes_total


def to_celsius(temperature: float) -> float:
    celsius = (temperature - 32) * 5/9
    return celsius


def to_farenheit(temperature: float) -> float:
    farenheit = (temperature * 9 / 5) + 32
    return farenheit


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
