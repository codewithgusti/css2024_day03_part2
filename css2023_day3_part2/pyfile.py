#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:03:24 2024

@author: dianachapter
"""

import numpy as np
import matplotlib.pyplot as plt

#  squares = np.arange(1,6)**2
#  print(squares)

# x = np.arange(1,6)
# y= x **2

# print(x.shape)
# print(y.shape)
# print(x*y)
# print('calculating  dot product')
# print(x.dot(y))
# print('calculating  cross product')
# print(np.matmul(x,y))
# plt.plot(x,y,"r*")
# plt.show()

# alist = [1,2,5,6,15,22]
# data = np.array(alist)
# print(data)
# data2 = data.reshape([2,3])
# data3 = np.reshape(data, [2,3])
# print("data 2")
# print(data2)
# print("data 3")
# print(data3)
# alist2 = [[1,2,5], [6,15,22]]
# data3 =np.array(alist2)
# data3 = np.array(alist2)
# data4 = np.matmul(data2.T,data3)
# print(data4)
# # cross product of matrices

# print("cross product")
# crossdata = np.cross(data2[0,:], data2[1,:])
# print(crossdata)

a=np.array([[1,2,3],[4,5,6],[7,8,-9]])
b= np.array([3,-4,2])
d=np.linalg.det(a)
if(d>0):
    print(f"d = {d} , so this matrix is solvable")
sol = np.linalg.solve(a, b)
