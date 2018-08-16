import os

os.chdir("/var/www/PythonMega/files/filehandling")

file=open("write.txt","w")
L = ['line 1','line 2', 'line 3']
for item in L:
    file.write(item + "\n")
file.close()

