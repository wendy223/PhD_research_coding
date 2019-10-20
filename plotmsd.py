import matplotlib.pyplot as plt
import csv
import pandas as pd
import os,os.path
x = []
y = []

import numpy
path = os.path.join(os.getcwd(), 'msd.UTSA')
print(path)
d = numpy.loadtxt(path,skiprows=1)
x = d[:,0]/1000
y = d[:,3]


plt.plot(x,y,'o-')
plt.xlabel('Time (ps)')
plt.ylabel('MSD ($A^2$)')
plt.legend()
plt.show()

