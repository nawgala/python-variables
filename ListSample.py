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

# from book Programming Python
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 50000, 'hardware']

people = [bob, sue]

# Modify list
for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20

for p in people: print(p[2])

# collect all the pay
pays = [person[2] for person in people]
print(type(pays))
print(pays)


# Map function
pays = map((lambda x: x[2]), people)
total  = sum(pays)
print(total)

NAME,AGE, PAY, JOB = range(4)
print(bob[NAME])
print(PAY, bob[PAY])