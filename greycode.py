#!/usr/bin/python


import sys
from pathlib import Path

symbols = [" ","_","-","","."]

name_of_script = sys.argv[0]		#First argument as the name of script [greycode.py]
src_file=sys.argv[1]			#Second argument as source file
new_file=sys.argv[2]			#Third argument as a new file

#read = open(src_file, 'r') 

def names():
    again = open(src_file, 'r')
    eol = len(again.readlines())
   
    read = open(src_file, 'r')
    
    for line in read:

        new=open(new_file+".txt", 'a')
        first = line.split()
        eol -= 1
        if eol == 0:
            sys.exit()

        for i in symbols:

                comb1=first[0]+i+first[1]
                comb2=first[1]+i+first[0]
                #print(comb1)
                #print(comb2)
                comb1str=''.join(comb1)
                comb2str=''.join(comb2)
                new.writelines(comb1str+"\n")
                new.writelines(comb2str+"\n")



src=Path(src_file)

if src.is_file():
    #file exists

    new = Path(new_file)

    if new.is_file():
        #new file exists
        print("Error -- Error -- Error")
        print("******Mentioned file is already exists******")

    else:
        #new file does not exist
        names()

else:
    #src file does not exist
    print("Error -- Error -- Error")
    print("The given file is not exists")
