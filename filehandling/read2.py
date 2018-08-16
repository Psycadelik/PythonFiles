import os

os.chdir("/var/www/PythonMega/files/filehandling")

file=open("fruit.txt","r")
content=file.read()
print(content)
file.seek(0)
content2=file.readlines()
print(content2)
content3=[len(i.strip()) for i in content2]
print(content3)
# print(len(content3[0]),len(content3[1]),len(content3[2]),len(content3[3]),len(content3[4]),len(content3[5]))