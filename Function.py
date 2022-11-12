def greeting(name = "sampath"):
    user = name
    if user is not '':
        user = input("What is your name ?: ")
    print("hello", user)
greeting()
greeting("Nawgala")


def print_kid_name(*kids):
    print(len(kids))

    (a, b) = kids
    print(a)
    print(b)
print_kid_name("Oneki", "Chenuka")

def kid_name(first, second):
    print(first)
    print(second)
kid_name(second="chenuka", first="oneki")