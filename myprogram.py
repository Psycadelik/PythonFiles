def age_foo(age):
    new_age = float(age) + 50
    return new_age


age = input("Enter your age: ")

if age_foo(age) > 100:
    print("c'est ne pas possible!")
else:
    print(age_foo(age))


