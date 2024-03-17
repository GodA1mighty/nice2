#while specified condition is True:
    #body of loop 

print(##########################################)

x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))


print(##########################################)


starting_attempt = 0
while starting_attempt != 3:
    input("Enter Your Login: ")
    starting_attempt += 1
print("Locked Out")


print(##########################################)


    #Infinite Loop  (stop loops is 'Control+C')
x = 0
while x % 2 == 0:
    x = x / 2
    print(x)
#No output

    #Stopping Infinite Loops
    #Only allows when the x isn't 0 so no infinite loop
if x != 0:
    while x % 2 == 0:
        x = x / 2
#No output

while x != 0 and x % 2 == 0:
    x = x / 2
#No output

while True:
    do_something_cool()
    if user_requested_to_stop():
        break
#This code will give an error because do_something_cool is not defined


print(##########################################)


multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5    #THE UPDATER
print("Done")


print(##########################################)


# This function counts the number of integer factors for a 
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a 
# factor (n*1). 
def count_factors(given_number):
    factor = 1
    count = 1
    if given_number == 0:
        return 0
    while factor < given_number:
        if given_number % factor == 0:
            count += 1
        factor += 1
    return count

print(count_factors(0)) # Count value should be 0
print(count_factors(3)) # Should count 2 factors (1x3)
print(count_factors(10)) # Should count 4 factors (1x10, 2x5)
print(count_factors(24)) # Should count 8 factors (1x24, 2x12, 3x8, and 4x6). 


# print(##########################################)


# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20.

# The function accepts a "given_number" variable through its
# parameters.
def addition_table(given_number):
	iterated_number = 1
	my_sum = 1
	while iterated_number <= 5:
		my_sum = given_number + iterated_number
		if my_sum > 20:
			break
		print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
		iterated_number += 1

addition_table(5)
addition_table(17)
addition_table(30)
# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None
