#! /usr/local/pacerepov1/python/2.7/intel-15.0/bin/ python

import numpy as np
import math

T = 323
Qgasc2h6 = 5986803877.72

def vibration(i):
    Qvib = 1/(1-np.exp(-1.44*float(i)/T))
    print(i,Qvib)
    return Qvib

with open('fre.dat') as f:
    vib = [ i for i in f.read().split()]

Qadvib = 1
for i in vib:
   Qadvib = vibration(i) * Qadvib

bo = Qadvib/Qgasc2h6
print(bo)
