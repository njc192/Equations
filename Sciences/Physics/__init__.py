from math import sqrt
from mpmath import *

from Sciences import PhysicsLabs
from Sciences.BaseUnitConverter import Unit

mp.prec = 20

'''
velocity = sqrt(Tension/(mass per unit length))
'''


def solve_velocity_tension_mu(tension, mu):
    return sqrt(tension / mu)


def solve_velocity_wavelength_freq(wav, freq):
    return freq * wav


def solve_tension(mu, velocity):
    return pow(velocity, 2) * mu


'''
by definition velocity = d/t and therefore lambda/period
'''


def solve_velocity_dist_over_time(wavelength, period):
    return wavelength / period


'''
velocity = (wavelength)*(frequency)
'''


def solve_wavelength(velocity, frequency):
    return velocity / frequency


def solve_frequency(velocity, wavelength):
    return velocity / wavelength


def solve_f_n_string(length, velocity, n):
    return (n * velocity) / (2 * length)


def solve_f_n_open_closed_tube(length, velocity, n):
    return (((2 * n) - 1) * velocity) / (4 * length)


def solve_wavelength_open_closed_tube_n(length, n):
    return (2 * n - 1) / (4 * length)


def solve_velocity_with_fn_open_closed_tube(length, n, freq):
    return (freq * 4 * length) / (2 * n - 1)


def solve_velocity_string(length, n, freq):
    return (freq * 2 * length) / n


def solve_n_with_L_frequency_velocity(length, frequency, velocity):
    return ((4 * length * frequency)/velocity + 1) / 2


def solve_wavelength_open_closed_tube(length):
    return 4 * length


'''
POWER

force/tension are interchangeable

omega(w) = 2pi / period
k = 2pi / wavelength
p_avg = (1/2)P_max
'''


def avg_power(amplitude, period, mu, force):
    omega = (2 * pi) / period
    return ((pow(amplitude, 2) * pow(omega, 2)) * sqrt(mu * force)) / 2


def super_positions(amplitude, wavelength, period, x, t):
    k = fdiv(fmul(2, mp.pi), wavelength)
    omega = fdiv(fmul(2, mp.pi), period)
    return 2 * amplitude * sin(k * x) * sin(omega * t)


if __name__ == '__main__':
    unit_converter = Unit()
    '''
    Sample Problem 1:
    '''

    # x = "Unknown"
    # length = x
    # mass = x
    # mu = 0.046  # kg/m
    #
    # wavelength = unit_converter.convert_to_base(130, "cm")
    # tension = 535  # Newtons
    #
    # velocity = solve_velocity_tension_mu(tension, mu)
    # freq = solve_frequency(velocity, wavelength)

    # print(f"Frequency: {freq}")

    '''
    Sample Problem 2:
    
    '''
    #
    # amplitude = 0.04
    #
    # period = .20
    # wavelength = 0.30

    '''
    a.) period = 0.2 s
    b.) frequency
    
    -- if you know the period(T) and the wavelength(lambda) then you can know the velocity (distance over time)
    -- if you know the period(T) then freq = 1/T
    '''

    # velocity = solve_velocity_dist_over_time(wavelength, period)
    #
    # freq1 = 1 / period
    # freq = solve_frequency(velocity, wavelength)

    # print(freq - freq1) #should be extrmely close to zero

    # print("velocity: ", velocity)
    #
    # print("freq: ", freq)

    '''
    for the time required problem you have to realize that the dot does not move horizontally, so you 
    are using the amplitude in this problem. the total distance would be 4 * amplitude.  
    '''
    #
    # x = 500 / .16
    #
    # t = x * period
    # print("time required : ", t)

    '''
    Quiz Question: 
    Which is the correct equation to use for determining the speed of a wave on a string c with tension FT, 
    mass m, and length L 
    
    mu = m/L
    
    tension = FT
    
    velocity = sqrt(tension/mu)
    '''
    # known = "known"
    # unknown = "unknown"
    # tension = known
    # length = known
    # mass = known
    #
    # velocity = unknown

    """
    Quiz Question: Find the frequency of vibration fn of a vibrating string of length 1.2m with a tension of 7N 
    and total string mass of 106g, vibrating in the fourth harmonic mode.  (Enter your calculated value in units of Hz) 
    """

    # mass = unit_converter.convert(106, 'g', "kg")
    # tension = 7
    # length = 1.2
    #
    # velocity = solve_velocity_tension_mu(tension, (mass / length))
    #
    # print("velocity ",velocity)
    # f_4 = (4 * velocity) / (2 * length)
    #
    # print(f_4)

    '''Quiz Question: 
    Find the tension FT in a vibrating string of length 1.2m, with a total string mass of 8g, 
    driven in the third harmonic mode by a frequency of 125Hz s
    '''
    #
    # length = 1.2
    # mass = unit_converter.convert(8, 'g', 'kg')
    #
    # f_3 = 125
    # mu = mass / length
    '''
    v = sqrt(T/mu)
    fn = nv/2L -> 125 = (3V)/2L -> V = 125*2L/3
    '''

    # velocity = (2 * length * 125) / 3
    #
    # print(velocity)
    #
    # tension = solve_tension(mu, velocity)
    #
    # print(tension)
    #
    #
    # freq = solve_f_n(length,100,3)
    #
    # print(freq)

    '''
    Physics Lab:
    Part 2 Open Closed tube
    500 Hz tuning fork
    '''
    #
    # lengths_500_hz = [.173, .498, .849]
    #
    # lengths_1000_hz = [.095, .249, .414]
    #
    # lengths = lengths_1000_hz
    # frequency = 1000  # 500
    # for i in range(len(lengths)):
    #     velocity = solve_velocity_with_fn_open_closed_tube(lengths[i], i + 1, frequency)
    #     wavelength = solve_wavelength_open_closed_tube_n(lengths[i], i + 1)
    #     diff = PhysicsLabs.percent_difference(velocity, 340)
    #     print(f"Velocity {i + 1}: {velocity} | Wavelength: {wavelength} | %difference= {diff}")
    #
    # string_mass = unit_converter.convert(2.26, 'g', 'kg')
    #
    # print(string_mass / 10)
    #
    # string_mass = string_mass / 10
    #
    # hanging_mass_50_g = unit_converter.convert(50, 'g', 'kg')
    #
    # hanging_mass_100_g = unit_converter.convert(100, 'g', 'kg')
    #
    # '''
    # Part 1:
    # Number 2.
    #
    # calculate Tension
    # '''
    #
    # freq_50_g = [25.5, 49.8, -1, 94.2]
    #
    # freq_100_g = [33.97, -1, 100, 135.6]
    #
    # curr_frequency = freq_50_g
    # hanging_mass = hanging_mass_50_g
    # print("mass: ", hanging_mass)
    #
    # Length = 1  # m
    #
    # mu = string_mass / Length
    # tensions = []
    # for i in range(len(curr_frequency)):
    #     print(f"n: {i + 1}")
    #
    #     print(f"frequency: {curr_frequency[i]}")
    #     velocity = solve_velocity_string(Length, i + 1, curr_frequency[i])
    #
    #     print(f"velocity: {velocity}")
    #     wavelength = solve_wavelength(velocity, curr_frequency[i])
    #
    #     print(f"wavelength: {wavelength}")
    #
    #     print("mu:", mu)
    #     tension = solve_tension(mu, velocity)
    #     print(f"tension: {tension}")
    #
    #     if curr_frequency[i] >= 0:
    #         tensions.append(tension)
    #
    # '''
    # calculate average tension
    # '''
    # total = 0
    # for i in range(len(tensions)):
    #     total += tensions[i]
    #
    # print("avg: ", total / len(tensions))
    #
    # print("Percent Error btwn Avg of 50g tensions, and expected: ", PhysicsLabs.percent_error(.54, .5))
    # print("Percent Error btwn Avg of 100g tensions, and expected: ", PhysicsLabs.percent_error(1.03, 1))
    #
    # lengths = [.185, .495, .85]
    #
    # for i in range(len(lengths)):
    #     wavelength = solve_wavelength_open_closed_tube(lengths[i])
    #     print("wavelength ", wavelength)
    #     print(f"n: {solve_n_with_L_frequency_velocity(lengths[i], 500,340)}")

