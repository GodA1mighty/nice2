# Ask the user two true or false questions
question1 = input("Is Python an interpreted language? (True or False) ")
question2 = input("Is Python case-sensitive? (True or False) ")

# Convert the user input to boolean values
answer1 = question1.lower() == "true"
answer2 = question2.lower() == "true"

# Use an if-else statement to print a unique response for each combination of answers
if answer1 and answer2:
    print("You are correct on both questions!")
elif answer1 and not answer2:
    print("You are correct on the first question, but wrong on the second one.")
elif not answer1 and answer2:
    print("You are wrong on the first question, but correct on the second one.")
else:
    print("You are wrong on both questions.")