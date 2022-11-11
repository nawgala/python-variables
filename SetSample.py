fruits = {1, 2,3,3}
print(fruits)
print(type(fruits))
# print(fruits[0]) TypeError  : 'set' does not support indexing
print(len(fruits))
vegetable = set(("beet", "leeks", "carrot"))
print(vegetable)
print(type(vegetable))
vegetable.add("pumpkin")
print(vegetable)
# vegetable.remove("leeks!") KeyError : 'leeks!'
# print(vegetable)
vegetable.remove("leeks")
print(vegetable)