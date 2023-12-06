# message = "sup bruv"
# binary = " ".join(format(ord(c), "b") for c in message)
# print(binary)
#
# binary_text = "1110011 1110101 1110000 100000 1100010 1110010 1110101 1110110"
# normal = "".join(chr(int(c, 2)) for c in binary_text.split(" "))
# print(normal)

user_input = input("Type Text Here: ")
binary = " ".join(format(ord(c), "b") for c in user_input)
print(binary)

user_input2 = input("Type Binary Here: ")
text = "".join(chr(int(c, 2)) for c in user_input2.split(" "))
print(text)


# Get input from the user
message = input("Enter a message: ")
binary_values = []  # Create an empty list to store binary values
# Iterate over each character in the message
for character in message:
    # Get the ASCII value of the current character
    ascii_value = ord(character)
    # Convert ASCII to binary
    binary_representation = format(ascii_value, "b")
    # Add the binary representation to the list
    binary_values.append(binary_representation)
# Join the binary values with a space in between
binary = " ".join(binary_values)
# Print the binary representation
print("Binary representation:", binary)

ascii_characters = []
user_input = input("Type Binary Here: ")
binary_substrings = user_input.split(" ")
for character in binary_substrings:
    decimal_value = int(character, 2)
    ascii_character = chr(decimal_value)
    ascii_characters.append(ascii_character)
text = "".join(ascii_characters)
print(text)
    





