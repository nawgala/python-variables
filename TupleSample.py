fruits = ("apple", "banana", "graphs", "banana")
# print(fruits(1)) TypeError : 'tuple' is not callable
print(fruits[0])
print(fruits[1])
print(fruits[2])
# print(fruits[4]) IndexError : tuple index out of range
print(fruits[3])
print(len(fruits))
letter = ('a',)
print(letter)
print("type:", type(letter))

# my_letter = tuple(1, 2)
# TypeError : tuple() takes at most 1 argument

my_letter = tuple((1, 2))
print(my_letter)
print(type(my_letter))
