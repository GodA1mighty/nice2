magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print('\n-----line5-----')
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!") #prints one "magician" variable at a time
    print(f"I can't wait to see your next trick, {magician.title()}.\n") #maintains the same variable
print("Thank you, everyone. That was a great magic show!") #outside the loop, so prints only once

print('\n-----line12-----')
for value in range(6):
    print(value)

print('\n-----line16-----')
for value in range(1, 5):
    print(value)

print('\n-----line20-----')
numbers = list(range(1, 6)) #places the range of numbers into a list
print(numbers)

print('\n-----line24-----')
even_numbers = list(range(2, 11, 2))#the third number in the range function (the second 2) will be used as the step size so going by 2's
print(even_numbers)

print('\n-----line28-----')
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

print('\n-----line35-----')
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

print('\n-----line41-----')
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print('\n-----line47-----')
squares = [value**2 for value in range(1, 11)]
print(squares)

print('\n-----line51-----')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[-3:])
print(players[0:4:1]) #the third slice is for skipping

print('\n-----line57-----')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print('\n-----line63-----')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\n-----line71-----')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print('\n-----line81-----')
dimensions = (200, 50) #this is a tuple, an unchangeable or an unmodifiable list
print(dimensions[0])
print(dimensions[1])

print('\n-----line86-----')
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

print('\n-----line91-----')
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100) #an example of a tuple changing by 'reassigning' it to the var dimensions...wtf?
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
