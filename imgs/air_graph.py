#!/bin/python3

import matplotlib.pyplot as plt
from math import *

timeLgth = 2880
timeCoe = timeLgth / (pi * 4)

xD = []
yD = []
for i in range(0, timeLgth, 40):
    xD.append(i)
    yD.append(sin(i/timeCoe)*0.5 + 1.5)

plt.title("Relative Intake of an Air Component")
plt.xlabel("Day to Day (minutes)")
plt.ylabel("Intake")
plt.plot(xD, yD, marker=".", linewidth=0.75, markersize=3.5, label="normal")

xD = []
yD = []
for i in range(0, timeLgth, 40):
    xD.append(i)
    yD.append(sin(i/timeCoe)*0.25 + 1.75)
plt.plot(xD, yD, marker=".", linewidth=0.75, markersize=3.5, label="promote")

xD = []
yD = []
for i in range(0, timeLgth, 40):
    xD.append(i)
    yD.append(sin(i/timeCoe)*0.25 + 1.25)
plt.plot(xD, yD, marker=".", linewidth=0.75, markersize=3.5, label="dampen")

plt.legend(loc="upper right")
plt.grid()
plt.show()

