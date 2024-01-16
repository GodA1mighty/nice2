number = 1
while number <= 5:
    print('*' * number)
    number = number + 1
print('Done')

print()

name = input("What is your name? ")
while name == "":
	print('Try again')
	name = input("What is your name? ")
print(f"Thank You {name}")

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