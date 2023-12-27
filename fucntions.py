def happy_birthday(name, age):
	print(f'Happy Brithday to {name}!')
	print(f'You are {age}')
	print('Happy Brithday to You!')
	print()

happy_birthday('Bro', 20)
happy_birthday('Steve', 30)
happy_birthday('Joe', 40)

print('~~~~~~~~~~~~~~~~~~~~~')

def display_invoice(username, amount, due_date):
	print(f'Hello {username}!')
	print(f'Your amount is {amount} due on {due_date}.')

display_invoice('BroCode', 42.50, '01/01')

print('~~~~~~~~~~~~~~~~~~~~~')

def add(x, y):
	z = x + y
	return z

def substract(x, y):
	z = x - y
	return z
	
def multiply(x, y):
	z = x * y
	return z

def divide(x, y):
	z = x / y
	return z

print(add(1, 2))
print(substract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

print('~~~~~~~~~~~~~~~~~~~~~')

def create_name(first, last):
	first = first.capitalize()
	last = last.capitalize()
	return first + '' + last

full_name = create_name('Bro', 'Code')
print(full_name)
