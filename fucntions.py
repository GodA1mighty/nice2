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


print('~~~~~~~~~~~~~~~~~~~~~')


#step 1: There are five functions defined
#Step 2: handle_payment Function: This function takes a payment_method as an argument. It uses a dictionary called 'dictionary' to map payment methods to their corresponding processing functions.
#Step 3: The handle_payment function is called with “paypal” and “money” as arguments.
#Step 4: When “paypal” is passed, the process_paypal function is executed, printing “Processing PayPal…”. When “money” is passed, since it’s not a key in the 'dictionary' dictionary, the default function process_error is executed, printing “Error. Please try again.”.

def handle_payment(payment_method):
    dictionary = {
        "credit_card": process_credit_card,
        "paypal": process_paypal,
        "crypto": process_crypto,
        "bank_transfer": process_bank_transfer,
        "default": process_error
    }
    return dictionary.get(payment_method, dictionary["default"])()

def process_credit_card():
    print("Processing credit card...")
def process_crypto():
    print("Processing crypto...")
def process_paypal():
    print("Processing PayPal...")
def process_bank_transfer():
    print("Processing bank transfer...")
def process_error():
    print("Error. Please try again.")

handle_payment("paypal")
handle_payment("money")
