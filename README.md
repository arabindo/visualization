`python-3.7.3` `NumPy-1.18.1` `bokeh-2.0.1` `matplotlib-3.1.3`

# Quantum Linear Harmonic Oscillator

Here I plot wave function of 1-d LHO.

The solution is assumed.

I use recurrence relation of Hermite polynomial, although one can use hermite polynomial direct from NumPy package.

The .py file is build with bokeh.

## Usage of lho.py

Using slider one can change the value of n, to get the nth state of the wave function (n is restricted to a upperlimit 150)

Use ``bokeh serve`` command to run the example by executing:

  ``bokeh serve lho.py``
  
 at your command prompt. Then navigate to the URL
    http://localhost:5006/lho
in your browser.

A sample of output:
![output](https://github.com/arabindo/QLho/blob/master/outimg/out_lho.png)


## Usage of lho_anim.ipynb

Open the file and execute line by line.
After executing the line, contain animate() function, you'll able to get the annimation.

### Screenshots are taken from animation:

![output](https://github.com/arabindo/QLho/blob/master/outimg/output2.png)
![output](https://github.com/arabindo/QLho/blob/master/outimg/output3.png)

****Note-***

_Here I use m=w=h_bar=1 for simplicity._

**Realistic values likely:**

*h_bar = 1.05e-34 J s*

*m=9.11e-31 kg(electron mass)*

*w=4.57e14 Hz*
