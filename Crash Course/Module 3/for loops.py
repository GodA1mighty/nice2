        #Structure:
# for element in long_list:
#   do_something(element)

# for element1 in long_list:
#   for element2 in long_list:
#     do_something(element1, element2)



print('\n======================')


print("        Exercise 1")
#Simple Printed List

#output:
# joe
# davis
# jan

friends = ["joe", "davis", "jan",]
for friend in friends:
    print(friend)


print('\n======================')



print("        Exercise 2")
#Multiplier

#output:
# 1
# 2
# 6
# 24
# 120
# 720
# 5040
# 40320
# 362880
# 362880

product = 1
for n in range(1,10):
    product = product * n
    print(product)
print(product)


print('\n======================')


print("        Exercise 3")
#Converter

#Output:
# 0 -17.77777777777778
# 10 -12.222222222222221
# 20 -6.666666666666667
# 30 -1.1111111111111112
# 40 4.444444444444445
# 50 10.0
# 60 15.555555555555555
# 70 21.11111111111111
# 80 26.666666666666668
# 90 32.22222222222222
# 100 37.77777777777778

def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x, to_celsius(x))


print('\n======================')



print("        Exercise 4")
#Domino Tiles

#Output:
# [0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6] 
# [1|1] [1|2] [1|3] [1|4] [1|5] [1|6] 
# [2|2] [2|3] [2|4] [2|5] [2|6]
# [3|3] [3|4] [3|5] [3|6]
# [4|4] [4|5] [4|6]
# [5|5] [5|6]
# [6|6]

for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()


print('\n======================')


print("        Exercise 5")
#Team Organizer

#Output:
# Dragons vs Wolves
# Dragons vs Pandas
# Dragons vs Unicorns
# Wolves vs Dragons
# Wolves vs Pandas
# Wolves vs Unicorns
# Pandas vs Dragons
# Pandas vs Wolves
# Pandas vs Unicorns
# Unicorns vs Dragons
# Unicorns vs Wolves
# Unicorns vs Pandas

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)


print('\n======================')



print("        Exercise 6")
#Looping Strings

#Output:
# H
# e
# l
# l
# o

greeting = 'Hello'
for char in greeting:
    print(char)

print()

#Output:
# H e l l o

greeting = 'Hello'
for char in greeting:
    print(char, end="")


print('\n======================')


print("        Exercise 7")
#Looping Strings

#Output:
# 0
# 1
# 2
# 3
# 4

greeting = 'Hello'
for i in range(len(greeting)):
	print(i)


print('\n======================')


print("        Exercise 8")

#Output:
# Hi Taylor
# Hi Luisa
# Hi Jamaal
# Hi Eli

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
        
greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

print()

#Output:
# Hi B
# Hi a
# Hi r
# Hi r
# Hi y

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends("Barry")


print('\n======================')


print("        Exercise 9")
#Looping Strings with While Loops

#Output:
# H
# e
# l
# l
# o

greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1

#or
#for letter in greeting:
    # print(letter)

print()

#Output:
# He
# el
# ll
# lo
# o

greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index+2])
    index += 1


print('\n======================')

print("        Exercise 10")
#List Comprehensions

#Output:
# [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)



		#Structure
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
