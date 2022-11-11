list = ["apple", "ball", "cat", 3]
number_list = [1, 2, 2, 3, 4 , 0, -1]
print(list)
print(number_list)
print(list[0])
print(list[1])
print(list[2])
# print(list[3]) # IndexError : list index out of range

# List method
number_list.append(3)
print(number_list)
number_list.sort()
print(number_list)

print(number_list.count(0))
print(number_list.count(2))

print(len(number_list))
print(type(number_list))