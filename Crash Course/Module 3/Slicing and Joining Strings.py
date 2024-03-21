        #SLICING STRINGS

shortest_African_Name = 'abcdefghijklmnopqrstuvwxyz'
print(shortest_African_Name[0])    #prints "a"
print(shortest_African_Name[2:10])    #prints "cdefghij"
print(shortest_African_Name[:])    #prints "abcdefghijklmnopqrstuvwxyz"

print()

print(shortest_African_Name[::2])    #prints "acegikmoqsuwy"
print(shortest_African_Name[::-1])    #prints "zyxwvutsrqponmlkjihgfedcba"
print(shortest_African_Name[::-4])    #prints "zvrnjfb"

print()

print(shortest_African_Name[-2])    #prints "y"
print(shortest_African_Name[-2:])    #prints "yz"


print('\n====================')


        #JOINING STRINGS

print("Hello" + " " + "world") #Prints “Hello world”

greetings = ["Hello", "world"]
print(" ".join(greetings))    # Prints "Hello world"

#concatenating strings and var
name = "Alice"
print("Hello, " + name + "!")    # Prints "Hello, Alice!"


print('\n====================')


        #SLICING AND JOINING STRINGS

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

print(format_phone("2025551212")) # Outputs: (202) 555-1212