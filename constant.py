import numpy as np
from scipy.integrate import quad

NAVO = 6.02204e23 #/mol
aB = 0.5217 #Angstron
q = 1.602192e-19 #C
m0 = 9.10938356e-31 #Kg
m = m0*0.19
eV = 1.602192e-19 #J
R = 1.98719 #cal/mole-K
kB = 1.380662e-23 # J/K(R/NAVO)
k = 8.617e-5 #eV kB/q
h = 6.62617e-34 #J-s
hbar = 1.05458e-34 #J-s(h/(2*pi))
Mp = 1.67264e-27 #kg Proton rest mass
c = 2.99792e8 #m/s speed of light in vacuum

epsilon_si = 11.7
epsilon_ox = 3.9
epsilon0 = 8.854187817e-12 #F/m, 1/(mu0c^2)

nint = 1.076e10*1e6 #m-3
T = 300.0
kT = kB*T/q #V thermal voltage at 300K

####################################

