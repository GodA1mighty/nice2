#Module 2
  #Expressions and Varibles
print(type("a"))
print(type(2))
print(type(2.5))


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

# The = equals assignment operator is used to assign a value to a
# variable.
my_variable = 3 * 5
print(my_variable)
#15
print(my_variable == 3 * 5)
#True

#Greater Than > and Less Than < Operators
print(11 > 3 * 3)
#True
print(4 / 2 > 8 - 4)
#False
print(4 / 2 < 8 - 4)
#True
print(11 < 3 * 3)
#False

#Greater Than or Equal to >= and Less Than or Equal to <= Operators
print(12 * 2 >= 24)
#True
print(18 / 2 >= 15)
#False
print(12 * 2 <= 30)
#True
print(15 <= 18 / 2)
#False


print()

  #Equality == and Not Equal To != Operators
# The == operator checks if the 2 values are exactly the same
print(32 == 30 + 2)
#True
print(5 + 10 == 6 + 7)
#False
print(10 - 4 != 10 + 4)
#True
print(9 / 3 != 3 * 1)
#False


    # Equality == and Not Equal to != Operators with Strings
# The == operator can check if two strings are equal to each other.
# If they are equal, the Python interpreter returns a True result.
print("a string" == "a string")
#True

print("4 + 5" == 4 + 5)
#False

print("rabbit" != "frog")
#True

event_city = "Shanghai"
print(event_city != "Shanghai")
#False

print("three" == 3)
#False


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
#True

# Unicode value of 66 and b has a Unicode value of 98. So, Python will 
# return a True result.
print("Brown" < "brown")
#True

print("sunbathe" > "suntan")
#False

# If two identical strings are compared using the less than < comparison
# operator, this will produce a False result because they are equal.
print("Lima" < "Lima")
#False

print("Five" < 6)
#error

print()
print('========================')
print()


    # PART 3: The Greater Than or Equal to >= and Less Than or
var1 = "my computer" >= "my chair"  #True
var2 = "Spring" <= "Winter"  #True
var3 = "pineapple" >= "pineapple"  #True
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"Spring\" less than or equal to \"Winter\"? Result: ", var2)
print("Is \"pineapple\" less than or equal to \"pineapple\"? Result: ", var3)
