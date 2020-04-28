`python-3.7.3` `NumPy-1.18.1` `bokeh-2.0.1`

# Quantum Linear Harmonic Oscillator

Here I plot interactive wave function of 1-d LHO.

I use recurrence relation of Hermite polynomial, although one can use hermite polynomial direct from NumPy package.

Using slider one can change the value of n, to get the nth state of the wave function (n is restricted to a upperlimit 150)

Use ``bokeh serve`` command to run the example by executing:

  ``bokeh serve lho.py``
  
 at your command prompt. Then navigate to the URL
    http://localhost:5006/lho
in your browser.

A sample of output:
![output](https://github.com/arabindo/QLho/blob/master/outimg/out_lho.png)

****Note-***

_Here I use m=w=h_bar=1 for simplicity._

**Realistic values likely:**

*h_bar = 1.05e-34 J s*

*m=9.11e-31 kg(electron mass)*

*w=4.57e14 Hz*
