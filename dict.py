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

#help(dict)
#.values(), .keys(), .pop(), .popitem(), .copy(), .get(), .setdefault(), .fromkeys(), .items(), .update, |=

users: dict = {0: 'Mario', 1: 'Luigi', 2: 'Wario',}
print(users, "\n")

# print(users.values())

# print(users.keys())

#removes only a specficied key and its value
# users.pop(2)
# print(users)

#displays the value from the popped key
# popped = users.pop(2)
# print(popped)
# print(users)

#pops the last item from the list
# users.popitem()
# users.popitem()
# print(users)

# my_copy = users.copy()
# print(users)
# print(my_copy)

#get the value from a specified key w/o creating an exception
# print(users.get(1))
# print(users.get(999, "Missing!"))
#if a key isn't found, you can add a value to non-listed items like "Missing!" to display the error. It will not create and add keys and values to the dict

# print(users.setdefault(0, '???'))
# print(users.setdefault(999, '???'))    #not only creates the missing key and its value but also adds it to the dict
# print(users)

# print(users.clear())

# people: list[str] = ['Peach', 'Toad', 'Bowser']
# users: dict = dict.fromkeys(people)
# print(users)

#items include key and value pairs
# print(users.items())
# for key, value in users.items():
#     print(key, value)

# users.update({2: 'Bob', 3: "James' sister"})
# print(users)
# print(users | {10: 'Spam', 11: 'Eggs'})#the '|' is a pipeline, a union operator

# users |= {12: 'Chicken', 13: 'Beef'}
# print(users)

print('-------------------------------')


student = {'name': 'John', 'age': 25, 'course': ['Math', 'CompSci'], 1: 'nice'}
print(student['name'])
print(student['course'])
print(student[1])

del student['age']
print(student)


print('-------------------------------')


d = {i:i**2 for i in range(1,6)}
print(d)

print()

ages = [18, 20, 26, 128]
d2 = {age:("young" if age <=100 else "old") for age in ages}
print(d2)

print()

old_price = {'Compound Effect': 12, 'Atomic Habit': 10, 'Twelve Pillars': 7}
dollar_to_pound = 0.82
new_price = {k:v*dollar_to_pound for k, v in old_price.items() if v<=10}
print(new_price)
