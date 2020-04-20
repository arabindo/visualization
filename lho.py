import numpy as np
import math
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure, output_file, show

#Function to get values of Hermite Polynomial

poly = {} #this dictionary is used to remember the hermite polynomials already calculated

def hermite(n):
    
    var = np.linspace(-20, 20, 10000)
    
    if (n in poly):
        return poly[n]
        
    elif  n==0:
        val_0 = 1
        return val_0
        
    elif n==1:
        val_1 = 2 * var 
        poly[1]= val_1
        return val_1
        
    else:
        val_n = ((2*var*hermite(n-1)) - (2*(n-1)*hermite(n-2)))
        poly[n]=val_n
        return val_n
    
    

#set up data
m = 1
w = 1
h_bar = 1
n=10
pi = np.pi

var = np.linspace(-20, 20, 10000)
A = hermite(n)*np.exp(-(var**2)/2)
psi = (1 / (math.pow(2, n) * math.factorial(n))**0.5) * ((m*w/(pi*h_bar))**0.25) * A
dp = ColumnDataSource(data=dict(x=var, y=psi))


#set up plot
TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"
p = figure(plot_height=600, plot_width=600,
            tools=  TOOLS, title="Linear Harmonic Oscillator",
            x_range=[-25,25], y_range=[-1.5,1.5],
            x_axis_label="x", y_axis_label="psi")
p.line(x='x', y='y', source=dp, legend_label="psi", line_color="blue")


#set up widgets
state = Slider(title="state of particle", value=10, start=0, end=150, step=1)


#set up callback
def update(attrname, old, new):
    pass
    
state.on_change('value', update)


#setup layout
inputs = column(state)

curdoc().add_root(row(inputs, p, width=800))
curdoc().title = "Wave function for Linear Harmonic Oscillator"
