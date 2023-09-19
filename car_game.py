error = "I don't understand that. Type 'help' for more options"
help = '''start - to start the car
stop - turn off the engine
quit - to exit'''
start = 'Car started, Ready to go!'
stop = 'Engine Off.'
user_input = 1
starting_text = 0

while user_input > starting_text:
    beginning_text = input('> ')
    if beginning_text == "start":
        print('Engine On')
    elif beginning_text == 'stop':
        print('Engine Off')
    elif beginning_text == 'help':
        print(help)
    else:
        print(error)
 
