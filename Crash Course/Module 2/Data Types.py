            #Module 2
print(type("a"))
print(type(2))
print(type(2.5))

print()

import typing
# Define a variable of type str
z: str = "Hello, world!"
print(z)
# Define a variable of type int
x: int = 10
print(x)
# Define a variable of type float
y: float = 1.23
print(y)
# Define a variable of type list
list_of_numbers: typing.List[int] = [1, 2, 3]
print(list_of_numbers)
# Define a variable of type tuple
tuple_of_numbers: typing.Tuple[int, int, int] = (1, 2, 3)
print(tuple_of_numbers)
# Define a variable of type dict
dictionary: typing.Dict[str, int] = {"key1": 1, "key2": 2}
print(dictionary)
# Define a variable of type set
set_of_numbers: typing.Set[int] = {1, 2, 3}
print(set_of_numbers)

print()
print('========================')
print()

def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
    
greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering")

print()

def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: ", sum)
#or
print("The sum of both areas is: " + str(sum))

print()
print('========================')
print()

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

print()

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)

print()

time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))

