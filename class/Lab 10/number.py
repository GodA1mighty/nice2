try:
    user_input = input("Enter a number: ")
    number = float(user_input)
    print("Entered Number:", number)

except ValueError:
    print("Error: Please enter a valid number.")