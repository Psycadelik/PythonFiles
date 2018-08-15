# function for calculating temperature from celsius degrees to farenheit : F =  C 9/5 + 32

def temp_to_farenheit(celsius):
    if celsius >= -273.15:
        farenheit= celsius*9/5 + 32
        return farenheit
    else:
        return "temperature is too low be measured"

temp = input("Please input the temperature in degrees celsius: ")

print("The temperature in farenheit is: ")
print(temp_to_farenheit(float(temp)))
