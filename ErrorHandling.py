try:
    print(x)
except NameError:
    print("variable is not defined")
except :
    print("something wrong")

try :
    print(x)
except NameError :
    print("Name error")
finally:
    print("Inside finally")

try:
    print("Opening the file")
    f = open("test.txt")
    try:
        f.write("test")
    except:
        print("Something wrong in writing")
except :
    print("file is not found")
finally:
    f.close()

x = "do something"

if not type(x) is int:
    raise TypeError("Integer expected")
