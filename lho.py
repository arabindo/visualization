import numpy as np

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
        val0 = 1
        return val0
        
    elif n==1:
        val_1 = 2 * var 
        val=val_1
        poly[1]= val
        return val
        
    else:
        value = ((2*var*hermite(n-1)) - (2*(n-1)*hermite(n-2)))
        poly[n]=value
        return value
    
    

#set up data




#set up plot



#set up widgets



#set up callback



#setup layout
