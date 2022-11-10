touple = ('a', "apple")
print(touple)
print(touple[0])
print(touple[1])
print(type(touple))
# print(touple[2])

list = [1,2,3,4,5,6,7]
print(list)
print(list[2])
print(list[2:])
print(list[:2])
# print(slice(0,3,list))
symbols = "$¢£¥€¤"
# for code in symbol :
#     codes.append(ord(code))
codes = [ord(symbol) for symbol in symbols]
print(codes)