# function for calculating temperature from celsius degrees to farenheit : F =  C 9/5 + 32

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