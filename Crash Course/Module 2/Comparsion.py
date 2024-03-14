#Module 2
  #Expressions and Varibles
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

#Comparing Things
print(10 > 1)
#True
print("cat" == "dog")
#False
print(1 != 2)
#True

#print(1 < "1") 
#Will return a type error

print(1 == "1")
#False
print("Yellow" > "Cyan" and "Brown" > "Magenta")
#False
print(25 > 50 or 1 != 2)
#True
print(not 42 == "Answer")
#True

print()

#Equality == and Not Equal To != Operators
print(32 == 30 + 2)  # The == operator checks if the 2 values are
True  # equal to each other. If they are equal,
# Python returns a True result.

print(5 + 10 == 6 + 7)  # If the two values are not equal, as in the
False  # expression 5+10 == 6+7 (or 15 == 13), Python
# returns a False result.

print(10 - 4 != 10 + 4)  # The != operator checks if the 2 values are
True  # NOT equal to each other. If true, Python
# returns a True result.

print(9 / 3 != 3 * 1)  # In this last example, 9/3 != 3*1 (or 3 != 3)
False  # is false. So, Python returns a False value.

# The = equals assignment operator is used to assign a value to a
# variable.
my_variable = 3 * 5  # Assigns a value to my_variable
print(my_variable)  # Printing the variable returns the
15  # value assigned to the variable.

# The == equality comparison operator checks if the values of the two
# expressions on either side of the == operator are equivalent to one
# another.
print(my_variable == 3 * 5)  # Printing the variable returns a Boolean
True  # True or False result.

#Greater Than > and Less Than < Operators
print(11 > 3 * 3)  # The > operator checks if the left value is
True  # greater than the right value. If true, it
# returns a True result.

print(4 / 2 > 8 - 4)  # If the > operator finds that the left value
False  # is NOT greater than the right value, the
# comparison will return a False result.

print(4 / 2 < 8 - 4)  # The < operator checks  if the left value is
True  # less than the right side. If true, the
# comparison returns a True result.

print(11 < 3 * 3)  # If the < operator finds that the left side is False
# NOT less than the right value, Python returns
False  # a False result.

#Greater Than or Equal to >= and Less Than or Equal to <= Operators
print(12 * 2 >= 24)  # The >= operator checks if the left value is
True  # greater than or equal to the right value.
# If one of these conditions is true,
# Python returns a True result. In this case
# the two values are equal. So, the comparison
# returns a True result.

print(18 / 2 >= 15)  # If the >= comparison determines that the left False
False  # value is NOT greater than or equal to the
# right, it returns a False result.

print(12 * 2 <= 30)  # The <= operator checks if the left value is
True  # less than or equal to the right value. In
# this case, the left value is less than the
# right value. Again, if one of the two
# conditions is true, Python returns a True
# result.

print(15 <= 18 / 2)  # If the <= comparison determines that the left
False  # value is NOT less than or equal to the right
# value, the comparison returns a False result.

print()

    # Equality == and Not Equal to != Operators with Strings
# The == operator can check if two strings are equal to each other.
# If they are equal, the Python interpreter returns a True result.
print("a string" == "a string")
True

# In this example, the equality == comparison is between "4 + 5" and
# 4 + 5. Since the left data type is a string and the right data type
# is an integer, the two values cannot be equal. So, the comparison
# returns a False result.
print("4 + 5" == 4 + 5)
False

# The != operator can check if the two strings are NOT equal to each
# other. If they are indeed not equal, then Python returns a True result.
print("rabbit" != "frog")
True

# In this example, the variable event_city has been assigned the string
# value "Shanghai". This variable is compared to a static string,
# "Shanghai", using the != operator. As, the strings "Shanghai" and
# "Shanghai" are the same, the comparison of "Shanghai" != "Shanghai"
# is false. Accordingly, Python will return a False result.
event_city = "Shanghai"
print(event_city != "Shanghai")
False

# This last example illustrates the result of trying to compare two
# items of different data types using the equality == operator. The
# two items are not equal, so the comparison returns False.
print("three" == 3)
False


print()
print('========================')
print()


    # PART 2: The Greater Than > and Less Than < Operators

# The greater than > operator checks if the left string has a higher 
# Unicode value than the right string. If true, the Python interprete
# returns a True result. Since W has a Unicode value of 87, and you can 
# easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. As this is true, Python will return a True 
# result.
print("Wednesday" > "Friday")
True

# The less than < operator checks if the left string has a lower 
# Unicode value than the right string. If you reference the Unicode 
# chart above, you can see that all lowercase letters have higher 
# Unicode values than uppercase letters. We can see that B has a 
# Unicode value of 66 and b has a Unicode value of 98. This 
# comparison is the same as 66 < 98, which is true. So, Python will 
# return a True result.
print("Brown" < "brown")
True

# If the strings have the same first few letters, the comparison will
# cycle through each letter of each string, from left to right until it 
# finds two letters that have different Unicode values. In this example, 
# both strings share the initial substring "sun", but then have 
# different letters with different Unicode values in the fourth place 
# in each string. So, the fourth letters 'b' and 't' of the two
# strings are used for the comparison. Since 'b' does not have a higher
# Unicode value than 't', the comparison returns a False result.
print("sunbathe" > "suntan")
False

# If two identical strings are compared using the less than < comparison
# operator, this will produce a False result because they are equal.
print("Lima" < "Lima")
False

# This last example illustrates the result of trying to compare two
# items of different data types using the less than < operator. The 
# greater than > and less than operators < cannot be used to compare

# two different data types.
# print("Five" < 6) print an error


print()
print('========================')
print()


    # PART 3: The Greater Than or Equal to >= and Less Than or
# Use the Unicode chart in Part 2 to determine if the Unicode values of 
# the first letters of each string are higher, lower, or equal to one
# another. 
var1 = "my computer" >= "my chair"
var2 = "Spring" <= "Winter"
var3 = "pineapple" >= "pineapple"
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)