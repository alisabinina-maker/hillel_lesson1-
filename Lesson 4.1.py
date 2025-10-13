number_list = [2, 0, 7 ,7, 0, 4, 5, 5, 0, 8 ]
non_zero_list = [x for x in number_list if x != 0]
zero_count = number_list.count(0)
zeros = [0] * zero_count
print(non_zero_list + zeros)