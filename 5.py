# my_set = [el for el in range(100, 105) if el%2 == 0]
# i = 0
# result = 1
#
# for el in my_set:
#     i = i + 1
#     result = result * my_set[i-2]
# print(my_set, result)

from functools import reduce

def my_func(prev_el, el):
    return prev_el * el

my_set = [el for el in range(100, 1001) if el%2 == 0]
print(reduce(my_func, my_set))
