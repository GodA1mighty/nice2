message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)


print("\n===================\n")


message = "This is a new message"
print(message)
message = "And another one"
print(message)


print("\n===================\n")


pets="Cats & Dogs"
print(pets.index("&"))    #5
print(pets.index("C"))    #0
print(pets.index("Dog"))    #7
print(pets.index("s"))    #3

print()

print("Dragons" in pets)    #False
print("Cats" in pets)    #True
print("Mountains".upper())    #MOUNTAINS
print("Mountains".lower())    #mountains

print()

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

print(" yes ".strip())    #.strip get rid of blank spaces
print(" yes ".lstrip())    #only gets rid of left blanks
print(" yes ".rstrip())    #only gets rid of right blanks

print()

print("The number of times e occurs in this string is 4".count("e"))    #counts the number of whatever is in the method
print("Forest".endswith("rest"))    #returns true or false if "rest" is in the string
print("Forest".isnumeric())    #return 'False'
print("12345".isnumeric())    #return 'True'

print()

print(int("12345") + int("54321"))

print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))

print("This is another example".split())


print("\n===================\n")


                #Formatting bullshit
name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
print(f"Hello {name}, your lucky number is {number}")
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

print()

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

print()

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))


print("\n===================\n")



print("\n===================\n")


                #Complex Shit
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain + email[index+len("@" + old_domain):]
        return new_email
    return email

# Example
email = "john.doe@example.com"
old_domain = "example.com"
new_domain = "example.org"
new_email = replace_domain(email, old_domain, new_domain)
print("Original Email:", email)
print("New Email:", new_email)


print("\n===================\n")


