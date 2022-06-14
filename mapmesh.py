import shutil
import os
import numpy as np
import math
from decimal import Decimal
present_workdir= os.getcwd()

fptr_MD = open("pipeorder1.msh", "r")
Database_lines_MD = fptr_MD.readlines()
#print(Database_lines_MD)

line_num = 0
search_phrase = "$Nodes"
for line in Database_lines_MD:
    line_num += 1
   
    if line.find(search_phrase)>=0:
        #print(line_num)
        offset_line_number = line_num+1;
        nodes_number =int(Database_lines_MD[line_num])
        break

fptr_MD.close()
source_file = os.path.join(present_workdir,'pipeorder1.msh')
dest_file = os.path.join(present_workdir,'pipemesh_mapo1.msh')
shutil.copy(source_file,dest_file)
f0=0.25
L=2.0
Xo=2.0
for i in range(nodes_number):
   datarow =Database_lines_MD[offset_line_number+i].split()
   
  
   if float(datarow[3])>=2.0 and float(datarow[3])<=4.0:
    rad = np.sqrt(float(datarow[1])**2+float(datarow[2])**2)
    theta = np.arctan2(float(datarow[2]),float(datarow[1]))
    s=rad*(1-f0*(1-math.cos(2*math.pi*(float(datarow[3])-Xo)/(L))))
    datarow[1]=s*math.cos(theta)
    datarow[2]=s*math.sin(theta)
    Database_lines_MD[offset_line_number+i] = "{} {} {} {} \n".format(datarow[0], float((datarow[1])), float(datarow[2]),float(datarow[3]))

    fptr_MD_2 = open("pipemesh_mapo1.msh", "w")
    fptr_MD_2.writelines(Database_lines_MD)
    fptr_MD_2.close()
   
   

