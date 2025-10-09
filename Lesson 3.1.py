example = input("Enter list items separated by spaces: ")


lst = example.split()


if len(lst) > 1:
    last_item = lst[-1]          # take the last item
    lst = [last_item] + lst[:-1] # move it to the front


print("Result:", lst)
