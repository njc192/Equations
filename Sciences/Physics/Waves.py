import os
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation
from IPython import display


#
# def draw_a_wave():
#     dx = 10
#
#     amplitude = 3
#     phase = -0.73
#     omega = (2 * np.pi) / 0.020
#     x = np.arange(-1 * dx, dx, dx / 100)
#
#     wave = amplitude * np.sin(k * x + phase)
#
#     # y1 = amplitude * np.sin(k * x + phase)
#     # y2 = amplitude * np.sin(k * x)
#     # resultant_wave = 2 * amplitude * np.cos(phase * 1 / 2) * np.sin(k * x + phase * (1 / 2))
#
#     plt.plot(x, y1, color='blue', linewidth=2.0, linestyle='-')
#     plt.plot(x, y2, color='pink', linewidth=2.0, linestyle='-')
#     plt.plot(x, resultant_wave, color='yellow', linewidth=2.0, linestyle='-')
#     plt.xlim([0, dx])
#     plt.xlabel('x (mm)')
#     plt.ylabel('Amplitude')
#     plt.grid(True, which='both')
#     plt.axhline(y=0, color='k')
#     plt.xticks(np.arange(0, 2 * dx, dx / 10))
#     plt.tight_layout()
#
#     plt.show()

def init_frame():
    ax.set_xlim(0, 10)
    ax.set_ylim(-5, 5)
    return line1, line2, line3


def animate(frame_number):
    x1data.append(frame_number)
    x2data.append(frame_number)
    x3data.append(frame_number)

    amplitude = 3
    k = (2 * np.pi) / 20  # 200pi rad/m
    phase = 0.5
    x = np.linspace(0, 10, 1000)
    y1 = amplitude * np.sin(k * frame_number + phase)

    y1data.append(y1)
    y2 = amplitude * np.sin(k * x)

    y2data.append(y2)
    resultant_wave = 2 * amplitude * np.cos(phase * 1 / 2) * np.sin(k * x + phase * (1 / 2))

    y3data.append(resultant_wave)

    line1.set_data(x1data, y1data)
    line1.set_color('yellow')

    line2.set_data(x2data, y2data)
    line2.set_color('green')

    line3.set_data(x3data, y3data)
    line3.set_color('blue')

    return line1, line2, line3,


fig, ax = plt.subplots()

print(fig)

x1data, y1data = [], []
x2data, y2data = [] , []
x3data, y3data = [] , []
# line1, = plt.plot([], [], lw=3)

line1, = plt.plot([], [], lw=3)
line2, = plt.plot([], [], lw=3)
line3, = plt.plot([], [], lw=3)
anim = animation.FuncAnimation(fig, animate, frames=100, blit=True, init_func=init_frame)

plt.show()



