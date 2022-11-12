class Person :
    def __init__(sel, name, age):
        sel.name = name
        sel.age = age

    def __str__(self) :
       return self.name + self.age

    def print_name(self) :
        print(self.name)
person = Person("sampath", 33)

print(person.name)
print(person.age)
person.print_name()

class Student(Person):
    pass

s = Student('jana', 10)

class Member(Person):
    def __init__(self,  name, age, no):
        # self.name = name
        # self.age = age
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.no = no

    def __str__(self):
        return str(self.no) + self.name + str(self.age)



m = Member("Kamala", 22, 22)
m.print_name()
print(m)