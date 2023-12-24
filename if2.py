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