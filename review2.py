-------------------------------------------------------------------------------
#character_length
character_length = input('''Type you shit nigga:
''')
if len(character_length) < 3:
    print('Too Short')
elif len(character_length) > 10:
    print('Too Long')
else:
    print('Shits Looks Good')

-------------------------------------------------------------------------------
#weight_conversion
weight = int(input('Weight: '))
unit = input('lb or kg: ')
if unit == 'lb':
    conversion = weight * 0.45
    print(f'{conversion} in kilograms')
else:
    conversion = weight / 0.45
    print(f'{conversion} in pounds')
    
-------------------------------------------------------------------------------
#if_statements
is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink Plenty of Water")
elif is_cold:
    print("It's a cold day")
    print("Bring a Sweater")
else:
    print('Normal Temperature Today')

print("Enjoy your day")

-------------------------------------------------------------------------------
#if_credit
bad_credit = False
good_credit = True
price = 1000000

if bad_credit:
    down_payment = price * 0.2
else:
    down_payment = price * 0.1
print(f'Down Payment: {down_payment}')

-------------------------------------------------------------------------------
#and_or_not_func
criminal_record = False
high_credit = True

if high_credit and not criminal_record:
    print('You are Eligible for a Loan')
#could use the 'and', 'or', and the 'not' function

-------------------------------------------------------------------------------
#character_limit
character_limit = 50

if character_limit < 3:
    print('Character Limit too Small')
elif character_limit > 50:
    print('Character Limit too Big')
else:
    print('nice')

-------------------------------------------------------------------------------
#while loop
i = 1
while i <= 5: #condition
    print('*' * i) #extra like displaying the product
    i = i + 1 #increment then it repeats starting from the beginning
              #of the while loop
print('Done')

-------------------------------------------------------------------------------
#infinte_loop
while user_input > starting_text:
    beginning_text = input('> ')
    if beginning_text == 'nice':
        print('very nice')
    else:
        print(error)
        
-------------------------------------------------------------------------------
#guessing_game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
else:
    print('Sorry, You Failed...')
    
-------------------------------------------------------------------------------
#car_game
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car started...")
    elif command == "stop":
        print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that...")
        
-------------------------------------------------------------------------------
#advance_car_game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that...")
        
-------------------------------------------------------------------------------
