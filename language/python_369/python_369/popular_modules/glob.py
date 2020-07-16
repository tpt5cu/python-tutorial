#GLOB

import glob 
  
  
print('Named explicitly:') 
for name in glob.glob('/home/geeks/Desktop/gfg/data.txt'): 
    print(name) 
  
# Using '*' pattern  
print('\nNamed with wildcard *:') 
for name in glob.glob('/home/geeks/Desktop/gfg/*'): 
    print(name) 
  
# Using '?' pattern 
print('\nNamed with wildcard ?:') 
for name in glob.glob('/home/geeks/Desktop/gfg/data?.txt'): 
    print(name) 
  
# Using [0-9] pattern 
print('\nNamed with wildcard ranges:') 
for name in glob.glob('/home/geeks/Desktop/gfg/*[0-9].*'): 
    print(name)