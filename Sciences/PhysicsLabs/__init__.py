import math
import random


def convert_cm_to_mm(value):
    return value * 10


def main():
    values = [.79, 9, 5.85, 6.68]
    for i in range(len(values)):
        print(convert_cm_to_mm(values[i]))


def toss_a_coin():
    random.seed(None)
    value = random.randint(0, 9999) % 2 == 0

    if value:
        return "H"
    return "T"


def percent_difference(m1, m2):
    return (abs(m1 - m2) / abs(average([m1, m2]))) * 100


def percent_error(measured, expected):
    return (abs(measured - expected) / abs(expected)) * 100


def average(values):
    tot = 0
    for i in range(len(values)):
        tot += values[i]

    return tot / len(values)


def circumference(diameter):
    circumference = 2 * math.pi * (diameter / 2)
    return circumference


def area(diameter):
    radius = diameter / 2
    return math.pi * pow(radius, 2)


def energy(wavelength):
    wav = wavelength * 0.01
    return ((6.63 * pow(10, -34)) * (3 * pow(10, 8))) / wav


if __name__ == '__main__':
    diameter = 0.02005

    print(energy(12.2))


