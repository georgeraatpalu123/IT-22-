#George Raatpalu
#Harjutus10
#02.11.22



import re
fh = open("Python.txt")
for line in fh:
    if re.search("^[a-z0-9]+[A-Z]{1}", line):
         print(line,end='')