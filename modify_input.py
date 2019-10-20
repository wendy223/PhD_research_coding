#! /usr/local/pacerepov1/python/2.7/intel-15.0/bin/ python

import re
from shutil import copyfile

copyfile('CONTCAR', 'POSCAR_original')

outfile = open('POSCAR','w')
allLines = file.readlines()

for line in allLines[0:7]:
    line = line.strip()
    s = line
    string = str(s)
    newLines = ''.join(string)
    print newLines
    outfile.write(newLines + '\n')

outfile.write('Selective Dynamics'+ ' \n' +'Direct'+ ' \n')


for line in allLines[8:(8+(len(allLines)-9)/2)]:
    line = line.strip()
    s = line
    string = str(s) + str(' F F F')
    newLines = ''.join(string)
    print newLines
    outfile.write(newLines + '\n')

