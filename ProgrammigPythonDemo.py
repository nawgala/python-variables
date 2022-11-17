bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 50000, 'hardware']

people = [bob, sue]
for person in people:
    print(person)

for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20

# for person in people: print(person[2])
pays = [person[2] for person in people]
print(type(pays))
print(pays)
print(sum(list(pays)))

people.append(['Tom', 50, 0, None])
print(len(people))

