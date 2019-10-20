#!/usr/bin/python

import ase.calculators.neighborlist as nl
from ase import *
import ase.io.vasp
import ase.io.cif
import glob
from ase.data import atomic_numbers
from ase.data import covalent_radii
from ase.visualize import view
import ase.calculators.neighborlist as nl
from ase.data import *
from ase import Atom
import shutil
import os, sys


for filename in glob.glob('*.cif'):
#    file = open(filename)
    atoms = ase.io.cif.read_cif(filename)
    #print atoms

#---------------------build radii of cutoffs for each atom---------------------
    cutoffs=[]
    for i in range(len(atoms)):
        #print covalent_radii[atomic_numbers[atoms[i].symbol]]
        cutoffs.append(covalent_radii[atomic_numbers[atoms[i].symbol]])
	    #print cutoff


#-------------------(first atom, we assume is metal)-----build the neighborlist for the 24th line atom-----------------------

    neighborlist = nl.NeighborList(cutoffs, self_interaction=False,bothways=True)
    neighborlist.update(atoms)


#-------------------how many metal atoms are in the MOF-----------------------

    repeat = ["Cu"]
    n = 0
    for i in range(len(atoms)):
        if atoms[i].symbol in repeat:
            #print "repeat"
            n = n + 1
        else:
	    break
    #print ("Total numbers of metal:{}".format(n))

   

#-------------------find the coordination number (neigboring list) for each metal in MOF-----------------------

    length = []
    for j in range(n):
        indices,offsets = neighborlist.get_neighbors(j)   # we are surposed the first atom is metal
    	neighboringsymbol = []
    	for i in range(len(indices)):
            #print("Symbol {} : index {}".format(atoms[indices.item(i)].symbol, indices.item(i) ))
            neighboringsymbol.append(atoms[indices.item(i)].symbol)
	    #print neighboringsymbol
        #print("MOF name: {}, metal :{}, neighbor number:{},symbol:{}".format(filename,j,len(indices), neighboringsymbol))
        length.append(len(indices))
    #print ("{}".format(length))


#-------------------check all coordination # are identical in MOF-----------------------
    
    def all_same(items):
        return all(x == items[0] for x in items)

#-------------------move *.cif into different folder-----------------------

    if all_same(length):
        #print "right"
        if len(indices) == 2:
            shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/2CN/" + filename)
    	elif len(indices) == 3:
	    shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/3CN/" + filename)
    	elif len(indices) == 4:
	    shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/4CN/" + filename)
    	elif len(indices) == 5:
	    shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/5CN/" + filename)
    	elif len(indices) == 6:
	    shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/6CN/" + filename)
    	elif len(indices) == 7:
	    shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/7CN/" + filename)
    	elif len(indices) == 8:
	    shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/8CN/" + filename)
	elif len(indices) == 9:
	    shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/9CN/" + filename)
        else:
            print('identical,Check it:{}'.format(filename))
    else:
        #print "wrong"
        shutil.copy("/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/" + filename,"/nv/hp13/wyou6/data/core-mof-july2014/cumof/allcumof/mixedCN/" + filename)
