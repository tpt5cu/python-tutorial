#GLOB

import glob 
  
  
print('Named explicitly:') 
for name in glob.glob('/home/geeks/Desktop/gfg/data.txt'): 
    print(name) 
  
# Using '*' pattern  
"""
An asterisk (*) matches zero or more characters in a segment of a name. 
For example, dir/*.
"""

print('\nNamed with wildcard *:') 
for name in glob.glob('/home/geeks/Desktop/gfg/*'): 
    print(name) 
#OR
for name in glob.glob('/home/geeks/Desktop/gfg/file_*'): 
    print(name) 
  
# Using '?' pattern 
"""The other wildcard character supported is the question mark (?). 
It matches any single character in that position in the name. For example,"""

print('\nNamed with wildcard ?:') 
for name in glob.glob('/home/geeks/Desktop/gfg/data?.txt'): 
    print(name) 
  
# Using [0-9] pattern 
print('\nNamed with wildcard ranges:') 
for name in glob.glob('/home/geeks/Desktop/gfg/*[0-9].*'): 
    print(name)