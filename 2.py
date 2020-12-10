my_list =  [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = []
i = 0

for el in my_list:
    i = i + 1
    if (i > 1) & (el > my_list[i-2]):
        new_list.append(el)

print(f"Новый список: {new_list}")