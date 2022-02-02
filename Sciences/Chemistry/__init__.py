from mpmath import *

from Sciences.BaseUnitConverter import Unit

mp.prec = 50

SPEED_OF_LIGHT = 3 * pow(mpf(10), 8)
PLANCKS_CONSTANT = mpf(6.63) * pow(mpf(10), -34)
AVOGADROS_NUMBER = mpf(6.022e23)
Ry = mpf(2.18e-18)


def print_vals(value):
    print(nstr(value, 3))


def get_frequency(wavelength):
    warning("meter")
    return fdiv(SPEED_OF_LIGHT, wavelength)


def get_nenergy(frequency, n):
    return n * PLANCKS_CONSTANT * frequency


def delta_energy(ni, nf):
    return Ry * (fdiv(1, pow(ni,2)) - fdiv(1, pow(nf, 2)))


"""
energy in Joules
frequency in s-1
"""


def solve_for_n_energy(energy, freq):
    return fdiv(energy, fmul(PLANCKS_CONSTANT, freq))


def get_wavelength(frequency):
    return fdiv(SPEED_OF_LIGHT, frequency)


def get_energy_using_wavelength(wavlen):
    freq = get_frequency(wavlen)
    return get_energy(freq)


def get_energy(frequency):
    return PLANCKS_CONSTANT * frequency


'''
E = hv
v = E/h
'''
def get_frequency_with_energy(energy):
    return fdiv(energy, PLANCKS_CONSTANT)



def warning(base_unit):
    return f"WARNING! THIS EQUATION ASSUMES THAT THE PASSED VALUE IS IN : {base_unit}"


units = Unit()
#
#
# wavelen = units.convert_to_base(535,"nm")
#
# print("Wavelength:")
# print_vals(wavelen)
#
#
# print("Frequency")
#
# freq = get_frequency(wavelen)
# print_vals(freq)
#
#
# print("Energy")
# print_vals(get_energy(freq))

#
# wavelength = units.convert_to_base(705, "nm")
# print("Energy = ", get_energy_using_wavelength(wavelength))

deltaE = delta_energy(3, 2)
print(deltaE)

freq = get_frequency_with_energy(deltaE)

wavelength = get_wavelength(freq)


print(wavelength)

# wavelength = get_wavelength(5.80e14)
#
# print(wavelength)

print(get_frequency(4500))