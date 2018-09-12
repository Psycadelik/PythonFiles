import os

os.chdir("/var/www/PythonMega/files/filehandling")

file=open("write3.txt","w")
number = [1,2,3]
for item in number:
    file.write(str(item) + "\n")
file.close()

# we have covered r , w and a , try out a+, r+ and w+