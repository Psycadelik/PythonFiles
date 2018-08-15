def currency_converter(rate,dollars):
    ksh=rate*dollars
    return ksh

d=input("Enter value in dollars: ")

r=input("Enter the conversion rate: ")

print("The value in Kenya Shillings is: ")
print(currency_converter(float(d), float(r)))
