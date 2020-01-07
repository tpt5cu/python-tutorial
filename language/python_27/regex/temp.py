import re, pathlib

path = pathlib.Path(__file__).parent / '1.txt'
#with open (path, "r") as text:
#    data = text.read()
#print(re.sub(r"(.)\1*", lambda x: "{}{}".format(len(x.group()), x.group(1)), data))
with open (path, "r") as text:
    data = text.read()
#   U2B3R2L3B3D3 
# "1U2B3R2L3B3D3"1
print( re.sub(r"(.)\1*", lambda x: "{}{}".format( x.group(1), len(x.group())),  data))
