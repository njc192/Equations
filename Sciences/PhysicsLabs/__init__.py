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


def theta_critical(n1, n2):
    rads = math.radians(n2/n1)
    return math.asin(rads)


def rays_solve_theta2(n1,n2,theta1):
    rads = math.radians(theta1)
    theta2 = math.asin((n1*math.sin(rads))/n2)
    return theta2


if __name__ == '__main__':

    '''
    LAB 3
    '''



