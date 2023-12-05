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