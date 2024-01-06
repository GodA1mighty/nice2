# dictionary = a collection of {key: value} pairs.
    #Ordered and changeable. no duplicates

#print(dir(capitals)) all attributes
#print(help(capitals)) explains all attributes

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

print(capitals.get("India"))
print(capitals.get("Japan"))

print()

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

print()

print(capitals)
print("updated list:")
capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China")
capitals.popitem()#remove the latest item
print(capitals)
#capitals.clear()#completely clears
print(capitals)

print()

keys = capitals.keys()#get only the keys, not the values
print(keys)
for key in capitals.keys():
    print(key)

print()

values = capitals.values()
print(values)
for value in capitals.values():#you only need this line to get the values in capital
    print(value)

print()

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")


print('-------------------------------')

