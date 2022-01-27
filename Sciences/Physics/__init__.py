from mpmath import *

from Sciences.BaseUnitConverter import Unit

mp.prec = 20

'''
velocity = sqrt(Tension/(mass per unit length))
'''


def solve_velocity_tension_mu(tension, mu):
    return sqrt(tension / mu)


def solve_velocity_lambda_freq(wav, freq):
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

def solve_f_n(length,velocity,n):
    return (n*velocity)/(2*length)

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

    length = 1.2
    mass = unit_converter.convert(8, 'g', 'kg')

    f_3 = 125
    mu = mass / length
    '''
    v = sqrt(T/mu)
    fn = nv/2L -> 125 = (3V)/2L -> V = 125*2L/3
    '''

    velocity = (2 * length * 125) / 3

    print(velocity)

    tension = solve_tension(mu, velocity)

    print(tension)


    freq = solve_f_n(length,100,3)

    print(freq)




