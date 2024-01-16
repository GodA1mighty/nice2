number = 1
while number <= 5:
    print('*' * number)
    number += 1
print('Done')

print()

name = input("What is your name? ")
while name == "":
	print('Try again')
	name = input("What is your name? ")
print(f"Thank You {name}")

print()

x = 0
while True:
    if x == 5:    #delete here
        break    #and here to create an infinte loop
    print(x)
    x += 1

print()

name = input('''Engage infinte loop with ""''')
while name == "":
	print('Try again')
print(f"Thank You {name}")

print()

age = int(input('Enter you age: '))
while age < 0:
	print("Age can't be negative")
	age = int(input('Enter you age: '))
print(f'You are {age} years old!')

print()

food = input("Enter your favorite food ('q' to quit)")
while not food == 'q':
	print(f'You like {food}!')
	food = input("Enter your favorite food ('q' to quit) ")
print('Program Ended')

print()

num = int(input("Enter a # between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"You picked the number {num}")

print()

number = 0
while number < 5:
    print(number)
    if number == 3:
        break    #stops all the code
    number = number + 1

print()

number = 0
while number < 5:
    print(number)
    if number == 6:
        break
    number = number + 1
else:    #activates only when the while loop is False
    print("No longer < 5")

print()

#A1 infinite loop
number = 0
while number < 10:
    print(number)
    if number == 6:
        continue    #when the if statement is true, it disregards the following code and repeats at the start of the while loop. so not being iterated by the number += 1 anymore
    number = number + 1
else:    #activates only when the while loop is False
    print("No longer < 10")

print()

#A2 prevented infinite loop
number = 0
while number < 10:
    number = number + 1
    if number == 6:
        continue
    print(number)
else:
    print("No longer < 10")
