#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is program is used to visualize a single valued continious function
and behavior of the derivative of the function with x and y simultaneously.

Created on Wed Dec 16 2020

@author: arabindo
"""

#importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation

#define the function here
def funct(x):
	z = np.sin(x) 
	return z

#find the derivative using central difference
def derivative(x):
	h = 1e-10
	dev = (funct(x+h) - funct(x-h))/(2*h)
	return dev  

#generating the data points
def data_gen(t=0):
	cnt = 0
	while cnt < 1000:
		cnt += 1
		t += 0.1
		yield t, funct(t), derivative(t)

#Setting up initial subplots      
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,3)
ax3 = fig.add_subplot(2,2,4)
plt.suptitle("$ sin(x) $",size=10)

ax1.set_xlim(0, 5) #setting up limit
ax1.set_ylim(-1.2, 1.2) 
ax1.set_xlabel('x') #setting up labels
ax1.set_ylabel('y')

line1b = Line2D([], [], color='red', linewidth=2)
#line1c = Line2D([], [], color='blue', marker='o', markeredgecolor='r')

ax1.add_line(line1b)
#ax1.add_line(line1c)
    
ax2.set_xlim(0, 5) #setting up limit
ax2.set_ylim(-1.2, 1.2)
ax2.set_xlabel('x') #setting up labels
ax2.set_ylabel("dy/dx")

line2b = Line2D([], [], color='blue', linewidth=2)
#line2c = Line2D([], [], color='blue', marker='o', markeredgecolor='r')
 
ax2.add_line(line2b)
#ax2.add_line(line2c)

ax3.set_xlim(-1.2, 1.2) #setting up limit
ax3.set_ylim(-1.2, 1.2)
ax3.set_xlabel('y') #setting up labels
ax3.set_ylabel("dy/dx")

line3b = Line2D([], [], color='green', linewidth=2)
#line3c = Line2D([], [], color='blue', marker='o', markeredgecolor='r')

ax3.add_line(line3b)
#ax3.add_line(line3c)
    
xdata, y1data, y2data = [], [], []

def init():

    line1b.set_data([],[])
    #line1c.set_data([],[])
    
    line2b.set_data([],[])
    #line2c.set_data([],[])
    
    line3b.set_data([],[])
    #line3c.set_data([],[])
    
    line = [line1b, line2b, line3b]
    return line
    
def animate(data):
	#update the data
	x, y1, y2 = data
	xdata.append(x)
	y1data.append(y1)
	y2data.append(y2)

	#change the limit of x and y axix 
	#if curve exceeds the pre assigned values

	xmin, xmax = ax1.get_xlim()

	y1min, y1max = ax1.get_ylim()

	y12min, y12max = ax2.get_ylim()

	y13min, y13max = ax3.get_xlim()
	y2min, y2max = ax3.get_ylim()

	#updating ax1 and ax2 subplots
	#when x limit exceeds

	if x >= xmax:
		ax1.set_xlim(xmin, 2*xmax)
		ax2.set_xlim(xmin, 2*xmax)

		ax1.figure.canvas.draw()
		ax2.figure.canvas.draw()
    
	#updating ax1 subplot when y limit exceeds
	if y1 >= y1max:
		ax1.set_ylim(y1min, 2*y1max)
		ax1.figure.canvas.draw()

	#updating ax2 subplot when y limit exceeds
	if y1 >= y12max:
		ax2.set_ylim(y1min, 2*y1max)
		ax2.figure.canvas.draw()
	
	#updating ax3 subplot when y limit exceeds
	if y2 >= y2max:
		ax3.set_ylim(y2min, 2*y2max)
		ax3.figure.canvas.draw()
	
	#updating ax3 subplot when x limit exceeds
	if y1 > y13max:
		ax3.set_xlim(y1min, 2*y1max)
		ax3.figure.canvas.draw()

	#update the plots
	line1b.set_data(xdata, y1data)
	
	line2b.set_data(xdata, y2data)

	line3b.set_data(y1data, y2data)
	
	return [line1b, line2b, line3b]

anim = animation.FuncAnimation(fig, animate, data_gen, blit=True, interval=50, repeat=False, init_func=init)
#anim.save("subanim.mp4")
plt.show()
