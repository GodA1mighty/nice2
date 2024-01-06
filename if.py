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


print(-------------)


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


print(-------------)


#use of parentheses ()
high_income2 = False
good_credit2 = True
student2 = False
if (high_income2 or good_credit2) and not student2:
    print("3Eligible")
else:
    print("3Not Eligible")


print(-------------)


age2 = 22
if age2 >= 18 and age2 < 65:
#or expressed like:
#if 18 <= age < 65:
    print("Eligible4")


print(-------------)


g = 9
h = 8
if g < h:
	print('g is less than h')
else:
	if g == h:
		print('g is equal to h')
	else:
		print('g is greater than h')


print(-------------)


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


print(-------------)


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


print(-------------)


connection = True
paid = True
internet = True
def go_online():
    if not connection:
        return 'No connection...'
    elif not paid:
        return 'User has not paid...'
    elif not internet:
        return 'No Internet...'
    else:
        return 'You are online'
message = go_online()
print(message)


print(-------------)


paid = True
internet = True
if not internet:
    print("No internet")
elif not paid:
    print("User has not paid")
else:
    print("You are online")


print(-------------)


#guard clauses
connection = True
paid = True
internet = True
online = True
def go_online():
    if not connection:
        print('No connection')
        return
    if not paid:
        print('User has not paid')
        return
    if not internet:
        print('No internet')
        return
    if not online:
        print('You are offline')
        return
    print('You are online')

go_online()


print(-------------)


age = 29
nationality = 'Indian'

if 18 < age < 30 and nationality == 'Indian':
    print('You are eligible for the exam. Exam fee is $1,500.')
elif 18 < age < 30 and nationality == 'American':
        print('You are eligible for the exam. Exam fee is $15.')
else:
    print("You are not eligible for the exam.")


print('\n-------------------\n')


numbers = [0,1,2]
answer = "yes" if len(numbers) > 5 else "no"
print(answer)


print('\n-------------------\n')


today = 'Sunday'
if today == 'Saturday' or today == 'Sunday':
    print("It's a holiday!")
elif today == 'Monday' or today == 'Friday':
    print("Work 2 hours extra.")
else:
    print("Normal work hours.")


print('\n-------------------\n')


x = False
if not x:
    print("x is false.")

print()

name = ''
if not name:
    print("No name.")
else:
    print(f"Your name is {name}.")

print()

names = ['John', 'Mike', 'Sarah']
if not names: #if the list, dictionary, or tuple is empty, then NOT operator will return True.
    print("No names.")
else:
    print(f"There are a total of {len(names)} names.")


print('\n-------------------\n')


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For exmaple, '', (), [].
# Any empty mapping. For example, {}.

# True Values:
# Fill in any of the false values

condition = False#<---change value here into "False", "None", "0", "''", "{}"
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


print('\n-------------------\n')


def do_one(x):
    print("one: x*1 = ", x*1)
def do_two(x):
    print("two: x*2 = ", x*2)
def do_three(x):
    print("three: x*3 = ", x*3)
def do_default(x):
    print("default: x = ", x)

#change value here
x = 3
if x == 1:
    do_one(x)
elif x == 2:
    do_two(x)
elif x == 3:
    do_three(x)
else:
    do_default(x)

actions = {1: do_one, 2: do_two, 3: do_three}
action = actions.get(x, do_default)
#vvvv same as ^^^^
action(x)


print('\n-------------------\n')


lang = input("What's the programming language you want to learn? ")
match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")


print('\n-------------------\n')


# def calculator(a,b,operator):
#     if operator=="add":
#         return a+b
#     if operator=="sub":
#         return a-b
#     if operator=="multiply":
#         return a*b
#     if operator=="division":
#         return a/b
# print(calculator(9,7,"sub"))

print()

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b

dict_calculator={
    "add":add,
    "sub":sub,
    "mutiply":multiply,
    "division":division,
}

print(dict_calculator["mutiply"](6,7))
print(dict_calculator["add"](3,7))


print('\n-------------------\n')

