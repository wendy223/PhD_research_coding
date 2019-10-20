#!/bin/bash
grep -oP '.{0,12}cm-1' OUTCAR |awk '{print $1}'>fre.dat
python bo.py

