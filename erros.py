def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by 0 is impossible"

# a = input("Input one figure :")
# b = input("Input another figure :")

print(divide(6,0))
