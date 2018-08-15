def str_length(str):
    if type(str) == int:
        return "c'est non integer!"
    elif type(str) == float:
        # length = len(str)
        return "float values dn't have len"
    else:
        return len(str)

# st = input("Input any word: ")

# if type(st) == int:
#     print("integers not allowed")
# else:
print(str_length("hi"))

