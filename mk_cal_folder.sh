#dir=/nv/hp13/wyou6/data/Research/xiaowa_50mofs/MOCKAR/test
#echo $dir/MOCKAR_ISIF3

#ls > name.dat


I=1
N=$(cat name.dat | wc -l)
N=`expr $N + 1`
#echo $N

while [ $I -lt $N ];
do
  folder=$(sed -n "${I}p" name.dat)
 # echo $folder
  cd $folder

  mkdir ${folder}_ISIF3
  mv * ${folder}_ISIF3
  mkdir ${folder}_ISIF32R ${folder}_H2O_R ${folder}_CO_R ${folder}_C2H4_R ${folder}_C2H6_R
  cp ./${folder}_ISIF3/{CONTCAR,POTCAR,INCAR,KPOINTS,bindingenergy.sh} ./${folder}_ISIF32R
  
  # cd MOF_ISIF32R to change CONTCAR by using python
  cd ./${folder}_ISIF32R
  python ~/change.py
  sed -i -e 's/ISIF = 3/ISIF = 2/g' INCAR
  m=${folder}_ISIF32R
  #echo $m
  sed -i -e 's/SYSTEM =.*/SYSTEM ='${m}' /g' INCAR
  sed -i -e 's/#PBS -N.*/#PBS -N '${m}'/g' bindingenergy.sh
  cd ../

  cp ./${folder}_ISIF32R/* ./${folder}_H2O_R/ 
  cp ./${folder}_ISIF32R/* ./${folder}_CO_R/ 
  cp ./${folder}_ISIF32R/* ./${folder}_C2H4_R/
 cp ./${folder}_ISIF32R/* ./${folder}_C2H6_R/

  # change the bindingenergy.sh (job name) and INCAR file for H2O,CO,C2H4 folder
  cd ./${folder}_H2O_R
  n=${folder}_H2O_R
  sed -i -e 's/#PBS -N.*/#PBS -N '${n}'/g' bindingenergy.sh
  sed -i -e 's/SYSTEM =.*/SYSTEM ='${n}' /g' INCAR
  sed -i -e 's/'${folder}'.*/'${n}' /g' POSCAR
  cd ../

  cd ./${folder}_C2H4_R
  n=${folder}_C2H4_R
  sed -i -e 's/#PBS -N.*/#PBS -N '${n}'/g' bindingenergy.sh
  sed -i -e 's/SYSTEM =.*/SYSTEM ='${n}' /g' INCAR
  sed -i -e 's/'${folder}'.*/'${n}' /g' POSCAR
  cd ../

  cd ./${folder}_CO_R
  n=${folder}_CO_R
  sed -i -e 's/#PBS -N.*/#PBS -N '${n}'/g' bindingenergy.sh
  sed -i -e 's/SYSTEM =.*/SYSTEM ='${n}' /g' INCAR
  sed -i -e 's/'${folder}'.*/'${n}' /g' POSCAR
  cd ../

  cd ./${folder}_C2H6_R
  n=${folder}_C2H6_R
  sed -i -e 's/#PBS -N.*/#PBS -N '${n}'/g' bindingenergy.sh
  sed -i -e 's/SYSTEM =.*/SYSTEM ='${n}' /g' INCAR
  sed -i -e 's/'${folder}'.*/'${n}' /g' POSCAR
  cd ../

  cd ../

  I=`expr $I + 1`
done  

 #cp -r $dir1/$dd/{CONTCAR,POTCAR} $dd/

#mkdir MOCKAR_ISIF3
#cp ../../MOCKAR_ISIF3/KPOINTS .
