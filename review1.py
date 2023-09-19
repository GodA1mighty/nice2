#basic math shit like adding/sub/div/multi
print(10 + 3)

#prints the float
print(10 / 3)

#prints the integer
print(10 // 3)

#prints the remander of the division (aka modulis)
print(10 % 3)

#rounds the pritned value
print(round(10 / 3))

#prints the exponentals
print(10 ** 3)


#augmented assignment operator
x = 10
x -= 3
print(x)


#list of all the functions/methods when you import math 'https://docs.python.org/3/library/math.html'
-------------------------------------------------
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
x = f'{first} [{last}] is a coder'
print(x)
-------------------------------------------------
customer_name = 'Fred'
message = 'Their name is '+customer_name
print(message)


name = input('Enter your name please: ')
print('Hello', name)


weight_lb = input('Weight: ')
weight_kg = int(weight_lb) * 0.4
print(weight_kg)
-------------------------------------------------
print('Item\tSales\ncar\t50\nboat\t10')
print('...and then Luke said "It\'s a trap."')
-------------------------------------------------
#time consuming way of printing longer length texts
print('Welcome to Nerves of Steel')
print()
print('Everybody stand up')
print('Stay standing as long as you dare.')
print('Sit down just before you think the time will end.')
#using triple quotes is better
print('''Welcome to Nerves of Steel

Everybody stand up
Stay standing as long as you dare.
Sit down just before you think the time will end. ''')
-------------------------------------------------
print('Hello World')
print("It's a Wonderful World")
print('''...and then Luke said, "It's a trap"''')
-------------------------------------------------
import time
import random

print('Welcome to self Time')
print()
print('The OBJ of the game is to not be a slow fuck')
print('A time will be displayed and it is your job to keep count')
print('Be the last one to sit and WIN!')

stand_time = random.randint(5, 20)

print('Stay standing for', stand_time, 'seconds.')

time.sleep(stand_time)

print('****TIME UP****')
-------------------------------------------------
import time
print("Rocket Ready for Launch in 10 Seconds")
time.sleep(5)
print("Launch in 5")
time.sleep(1)
print("Launch in 4")
time.sleep(1)
print("Launch in 3")
time.sleep(1)
print("Launch in 2")
time.sleep(1)
print("Launch in 1")
time.sleep(1)
print("Pshhhhhh!")
-------------------------------------------------
import time
time_text = input('Enter the alarm time in seconds: ')
time_int = int(time_text)
print('Alarm Set')
time.sleep(time_int)
print('Time is up')
#or
import time
time_int = int(input('Enter the alarm time in seconds: '))
print('Alarm Set')
time.sleep(time_int)
print('Time is up')
-------------------------------------------------
import random
print('You have rolled:',random.randint(1,6))
-------------------------------------------------
x = 'i does what i likes'
print(x[:])

x = 'i does what i likes'
print(x[0:5])

x = 'i does what i likes'
print(x[-5])

x = 'i does what i likes'
print(x.find('i'))

x = 'i does what i likes'
print(len(x))

x = 'i does what i likes'
print('does' in x)

x = 'i does what i likes'
print(x.replace('likes', 'loves'))

x = 'i does what i likes'
print(x.upper())

x = 'i does what i likes'
print(x.lower())
-------------------------------------------------
1. what is 10 * 3?
2. what is the float value of 10 / 3?
3. what is the integer of 10 / 3?
4. what is the remainder of 10 / 3?
5. what is the rounded value of 10 / 3?
6. what is 10 to the power of 3
7. use an augmented assignment operator

8. format the phrase, "John Mayer is a Guitarist" into having square brackets
around 'Mayer'
9. create a customer name, add that name to the phrase, "Their name is "
10. ask for a name then greet them
11. ask for weight in kg, then convert into lb

12. organize a list containing: 10 iphones, 20 androids, and 100 nokia's
13. use single, double, and triple quotes

14. create gun stickin game
15. create a rocket launch program
16. create a configurable alarm
17. simulate a single dice roll

Use the phrase 'I does what I likes' for question 18-26
x = 'I does what I likes'

18. Copy the phrase exactly using brackets
19. What is the character of the 3rd through 8th character inthe phrase?
20. Using negative integers, what is the 2nd letter from the last?
21. Find the letter 'o'
22. How many characters are in the phrase?
23. Is it true that there is a 'o' in the phrase?
24. Replace the word 'likes' to 'loves'
25. Turn all characters in the phrase uppercase
26. Turn all characters in the phrase lowercase
----------------------------------------------------
