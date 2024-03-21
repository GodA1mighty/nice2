        #Structure:
# for element in long_list:
#   do_something(element)

# for element1 in long_list:
#   for element2 in long_list:
#     do_something(element1, element2)



print('\n======================')


print("        Exercise 1")
#Simple Printed List

friends = ["joe", "davis", "jan",]
for friend in friends:
    print(friend)


print('\n======================')



print("        Exercise 2")
#Multiplier

product = 1
for n in range(1,10):
    product = product * n
    print(product)
print(product)


print('\n======================')


print("        Exercise 3")
#Converter

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))


print('\n======================')



print("        Exercise 4")
#Domino Tiles

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


print('\n======================')


print("        Exercise 5")
#Team Organizer

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)


print('\n======================')



print("        Exercise 6")
#Looping Strings

greeting = 'Hello'
for char in greeting:
    print(char)

print()

for char in greeting:
    print(char, end="")


print('\n======================')


print("        Exercise 7")
#Looping Strings

for i in range(len(greeting)):
	print(i)


print('\n======================')


print("        Exercise 8")

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
        
greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

print()

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends("Barry")


print('\n======================')


print("        Exercise 9")
#Looping Strings with While Loops

greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1

print()

greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index+2])
    index += 1


print('\n======================')

print("        Exercise 10")
#List Comprehensions

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)




# for x in range(2):
#     print("This is the outer loop iteration number " + str(x))
#     for y in range(3+1):
#         print("Inner loop iteration number " + str(y))
#     print("Exit inner loop")

#Output:
# This is the outer loop iteration number 0
# Inner loop iteration number 0
# Inner loop iteration number 1
# Inner loop iteration number 2
# Inner loop iteration number 3
# Exit inner loop
# This is the outer loop iteration number 1
# Inner loop iteration number 0
# Inner loop iteration number 1
# Inner loop iteration number 2
# Inner loop iteration number 3
# Exit inner loop