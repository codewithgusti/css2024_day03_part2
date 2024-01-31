#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:24:20 2024

@author: dianachapter
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("noisydata.csv", skiprows = 1, delimiter=",")
data_avg = np.mean(data,0)
print("average of columns")
print(data_avg)
pressure = data[:,0]
flowrate = data[:,1]
fit=np.polyfit(pressure,flowrate,2)
flowfit=np.polyval(fit,pressure)
plt.plot(pressure,flowrate,"go")
plt.plot(pressure,flowfit,"k-")
plt.xlabel("pressure (Pa")
plt.ylabel("flow  rate ($m^3 /s$")

plt.show()