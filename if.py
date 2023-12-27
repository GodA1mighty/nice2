#standard variant
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

#condensed version
message1 = "Eligible1" if age >= 18 else "Not Eligible1"
print(message1)

print()

#using operators: or, and, not,
high_income = False
good_credit = True
student = True
if high_income or good_credit:
    print("2Eligible")
    if not student:
        print("22Eligible")
    elif good_credit and student:
        print("bing")
else:
    print("2Not Eligible")

print()

#use of parentheses ()
high_income2 = False
good_credit2 = True
student2 = False
if (high_income2 or good_credit2) and not student2:
    print("3Eligible")
else:
    print("3Not Eligible")

print()

age2 = 22
if age2 >= 18 and age2 < 65:
#or expressed like:
#if 18 <= age < 65:
    print("Eligible4")

print()

g = 9
h = 8
if g < h:
	print('g is less than h')
else:
	if g == h:
		print('g is equal to h')
	else:
		print('g is greater than h')

print()

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

print()

# Ask the user two true or false questions and convert the input to boolean values
questions = ["Is Python an interpreted language?", "Is Python case-sensitive?"]
answers = [input(q + " (True or False) ").lower() == "true" for q in questions]

# Use an if-else statement to print a unique response for each combination of answers
responses = [
"You are wrong on both questions.", 
"You are wrong on the first question, but correct on the second one.", 
"You are correct on the first question, but wrong on the second one.", 
"You are correct on both questions!"]

print(responses[answers[0] * 2 + answers[1]])

peepee