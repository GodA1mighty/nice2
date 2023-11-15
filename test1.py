message = "Hello World!"
binary = " ".join(format(ord(z), "b") for z in message)
print(binary)

binary_text = "1001000 1100101 1101100 1101100 1101111 100000 1010111 1101111 1110010 1101100 1100100 100001"
normal = "".join(chr(int(z, 2)) for z in binary_text.split(" "))
print(normal)
