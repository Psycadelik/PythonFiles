# function for calculating temperature from celsius degrees to farenheit : F =  C 9/5 + 32
"""
This file is written in python strict
"""

import os

os.chdir("/var/www/PythonMega/files/filehandling")
def temp_to_farenheit(celsius):
    if celsius >= -273.15:
        farenheit= celsius*9/5 + 32
        return farenheit
    else:
        return "temperature is too low be measured"

temperatures=[10,-20,-289,100]

for temp in temperatures:
    i=temp_to_farenheit(temp)
    print(i)
    # for item in file:
    # file=open("write4.txt","w")
        # file.write(str(item) + "\n")
    # file.close()
