import numpy as np
import sys
import glob, os

old = sys.argv[1]
new = sys.argv[2]

print old
print new


## my example change Hello to Hi

for file in os.listdir("./"):
    if file.endswith('.txt'):
        print file
        f = open(file,'r')
        data = f.read()
        ##print data
        new_data = data.replace(old, new)
        ##print new_data
        f2 = open('2.txt', 'w')    
        f2.write(new_data)
        f2.close()