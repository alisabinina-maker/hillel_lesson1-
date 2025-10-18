import keyword
import string

name = input("Enter a variable name: ")

new_name_filter = string.punctuation.replace("_", "")
# 1. Can't start with a digit
if name[0].isdigit():
    print(False)
# Uppercase letter
elif not name.lower() == name:
    print(False)
elif name in keyword.kwlist:
    print(False)
elif "__" in name:
    print(False)
elif  "  "  in name:
    print(False)
elif name:
    for element in name:
        if element in new_name_filter:
            print(False)
            break
        else: print("True")


