num = int(input("type 5 digit number"))

d5 = num % 10
d4 = (num // 10) % 10
d3 = (num // 100) % 10
d2 = (num // 1000) % 10
d1 = num // 10000

reversed_num = d5 * 10000 + d4 * 1000 + d3 * 100 + d2 * 10 + d1

print(reversed_num)

