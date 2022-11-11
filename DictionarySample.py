alphebet = {'a' : "apple",
            'b' : "bat",
            'b' : "bat",
            'b' : "bat",
            'b' : "baat",
            'c' : "cat",
            'f' : False}
print(alphebet)
print(len(alphebet))
print(type(alphebet))
# print(alphebet[0]) only from python 3.7, other versions are unorderd
print(alphebet.pop('a'))
alphebet['d'] = "dog"
print(alphebet)


for x in alphebet:
    print(alphebet[x])

alphebet.setdefault('d', True)
print(alphebet)
alphebet.clear()
print(alphebet)
