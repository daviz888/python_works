#Counting to twenty
#  for value in range(1,21):
#     print(value)

# One Million list
# million = list(range(1,1000001))

# Summing a Million
# low = min(million)
# high = max(million)
# total = sum(million)

# print(low)
# print(high)
# print(total)

# Odd Numbers
# odd_numbers = list(range(1,21,2))
# print(odd_numbers)

# multiples of 3
cube = []
for value in range(3,31):
    cube.append(value**3)

print(cube)

cube2 = [value**3 for value in range(1, 11)]
print(cube2)