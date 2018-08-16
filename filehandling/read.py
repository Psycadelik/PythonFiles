import os
os.chdir("/var/www/PythonMega/files/filehandling")
file=open("num.txt", "r")
content=file.read()
print(content)
file.seek(0)
content=file.readlines()
# print(content)
content=[i.rstrip("\n") for i in content]
print(content)
file.close()