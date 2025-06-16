from itertools import zip_longest

a = ['x', 'y']
b = [1, 2, 3]

result = list(zip_longest(a, b, fillvalue='N/A'))
print(result)  # [('x', 1), ('y', 2), ('N/A', 3)]