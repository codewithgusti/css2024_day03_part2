#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:50:14 2024

@author: dianachapter
"""

import numpy as np
import matplotlib.pyplot as plt
n=30
x = np. random. uniform (size=n)
y = np. random. uniform(size=n)
print(sum(x*x+y*y <=1)/n*4)
plt. plot (x[x*x+y*y<=1] ,y [x*x+y*y<=1], "bo" ) 
plt. plot (x[x*x+y*y>1], y [x*x+y*y>1], "ro")
plt.savefig("pi.jpg")
plt.title("Calculating $\pi$")
plt. show