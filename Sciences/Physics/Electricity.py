import math

import numpy

from Sciences.BaseUnitConverter import Unit
from sympy import symbols,solve



def F_E(q1,q2, d):
    return k*((q1*q2)/pow(d,2))

def print_me(letter, value):
    print(letter, "->", value )


k = 8.99e9
unit = Unit()
#
# q1 = unit.convert_to_base(558, 'nm')
# q2 = q1
#
# q3 = unit.convert_to_base(94.4, 'nm')
# q4 = q3
# a = 6.65e-2
# d = math.sqrt(pow(a,2) + pow(a,2))
# ONE_OVER_ROOT2 = 1/math.sqrt(2)
# f2x = ONE_OVER_ROOT2 * F_E(q2,q3,d)
# f2y = ONE_OVER_ROOT2 * F_E(q2,q3,d)
# f1 = F_E(q1,q3,a)
# f4 = F_E(q3,q4,a)
# sum_Fx = f2x + f4
# sum_Fy = f2y - f1
#
#
# print(f2x)
# print(f4)


q2 = 8e-19
q3 = q4 = 4.8e-19
cos_theta = numpy.cos(numpy.radians(10))
d = 0.03
h = d/numpy.cos(numpy.radians(36))
h_squared = pow(h,2)

d_squared = pow(d,2)

x1 = q3*cos_theta / h_squared
x2 = q4*cos_theta / h_squared


solve_me = q2/ (x1 + x2)

solve_me = d_squared - solve_me

x =-1
q1 = -8e-6


V_x = (k*-1*q1)/(x + 2) + (k*q1)/(-1*x + 2)

print(V_x)


E_0 = k*-1*q1/(2*2) + k*q1/(2*2)

print(E_0)

change =x