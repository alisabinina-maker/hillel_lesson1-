variables = input("Enter list items separated by spaces: ")
lst = variables.split()

if len(lst) == 0:
    result = [[], []]
else:
    middle = (len(lst) + 1) // 2
    first = lst[:middle]
    second = lst[middle:]
    result = [first, second]

print("Result:", result)