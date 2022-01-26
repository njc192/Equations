from mpmath import *

from Sciences.BaseUnitConverter import Unit

mp.prec = 50

SPEED_OF_LIGHT = 3 * pow(mpf(10), 8)
PLANCKS_CONSTANT = mpf(6.63) * pow(mpf(10), -34)
AVOGADROS_NUMBER = mpf(6.022e23)


def print_vals(value):
    print(nstr(value, 3))


def get_frequency(wavelength):
    warning("meter")
    return fdiv(SPEED_OF_LIGHT, wavelength)

def get_nenergy(frequency,n):
    return n*PLANCKS_CONSTANT*frequency

"""
energy in Joules
frequency in s-1
"""
def solve_for_n_energy(energy,freq):
    return fdiv(energy,fmul(PLANCKS_CONSTANT,freq))


def get_wavelength(frequency):
    warning("second")
    return fdiv(SPEED_OF_LIGHT,frequency)


def get_energy_using_wavelength(wavlen):
    warning("meter")
    freq = get_frequency(wavlen)
    return get_energy(freq)


def get_energy(frequency):
    return PLANCKS_CONSTANT * frequency


def warning(base_unit):
    return f"WARNING! THIS EQUATION ASSUMES THAT THE PASSED VALUE IS IN : {base_unit}"


units = Unit()


wavelen = units.convert_to_base(535,"nm")

print("Wavelength:")
print_vals(wavelen)


print("Frequency")

freq = get_frequency(wavelen)
print_vals(freq)


print("Energy")
print_vals(get_energy(freq))