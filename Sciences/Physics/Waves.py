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
    for line in lines:
        line.set_data([], [])
    return lines


def animate(frame_number):
    value = frame_number/10
    x1data.append(value)
    x2data.append(value)
    x3data.append(value)

    amplitude = 3
    k = (2 * np.pi) / 20  # 200pi rad/m
    phase = 0.5
    y1 = amplitude * np.sin(k * value + phase)

    y1data.append(y1)
    y2 = amplitude * np.sin(k * value)

    y2data.append(y2)
    resultant_wave = 2 * amplitude * np.cos(phase * 1 / 2) * np.sin(k * value + phase * (1 / 2))

    max_min.append(resultant_wave)
    y3data.append(resultant_wave)

    if abs(resultant_wave) == -5.8015133080021455:
        print(value)

    xlist = [x1data, x2data, x3data]
    ylist = [y1data, y2data, y3data]

    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum])  # set data for each line separately

    max_min.sort()
    # print("max", max_min[len(max_min)-1])
    # print("min", max_min[0])

    return lines


fig = plt.figure()
ax1 = plt.axes(xlim=(0, 100), ylim=(-10, 10))
max_min = []
period = 0.0001
freq = 1/period

line, = ax1.plot([], [], lw=2)
x1data, y1data = [], []
x2data, y2data = [], []
x3data, y3data = [], []

plotlays, plotcols = [3], ["yellow", "green", "blue"]

lines = []
for index in range(3):
    lobj = ax1.plot([], [], lw=2, color=plotcols[index])[0]
    lines.append(lobj)

anim = animation.FuncAnimation(fig, animate, frames=1200,interval=period, blit=True, init_func=init_frame)

plt.show()




