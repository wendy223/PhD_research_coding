import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy
import matplotlib
import glob, os


path = os.getcwd()
print(path)

#'/nv/hp13/wyou6/scratch/utsa280/mayank/10initial/fc2h4/1'
#os.chdir("/1")

text_files = [f for f in os.listdir(path) if f.endswith('.txt')]

for i in text_files:
	d = numpy.loadtxt(i)
	plt.plot(d[1,:],d[0,:],'o--',label=i)
	plt.legend(loc='best')

plt.xlabel('time(ps)',fontsize=26)
plt.ylabel('msd($A^2$)',fontsize=26)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()	