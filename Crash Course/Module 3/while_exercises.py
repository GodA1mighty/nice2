print("    Exercise 1")
#Output:
#x
#xx
#xxx
#xxxx
#xxxxx

x = 0
while x < 6:
    print("x" * x)
    x += 1
print("done")


print('\n======================\n')


print("    Exercise 2")
# Output:
# Not there yet, x=0
# Not there yet, x=1
# Not there yet, x=2
# Not there yet, x=3
# Not there yet, x=4
# x=5

z = 0
while z < 5:
    print("Not there yet, x=" + str(z))
    z += 1
print("Done!\nx=" + str(z))


print('\n======================\n')


print("    Exercise 3")
# Output:
# Enter Login: nah
# Enter Login: blah
# Enter Login: ni
# Locked Out

print('''"uncomment the code to see"''')
# starting_attempt = 1
# while starting_attempt < 4:
#     input("Enter Login: ")
#     starting_attempt += 1
# print("Locked Out")


print('\n======================\n')


print("    Exercise 4")
# Output:
#Create an infinte loop with a break

b = 0
while b == 0:
    print(b)
    break


print('\n======================\n')


print("    Exercise 5")
#Output:
# 5
# 10
# 15
# 20
# 25
# 30
# 35
# 40
# 45
# 50
# Done

multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print('done')


print('\n======================\n')


print("    Exercise 5")

#Find the primes of these numbers: 2, 4, 8
# Output:
# Number of Factors:
# 0
# 2
# 3
# 12

#Factor Counter
def factor_counter(given_number):
    factor = 1
    current_count = 1
    if given_number == 0:
        return 0
    while current_count < given_number:
        if given_number % current_count == 0:
            factor += 1
        current_count += 1
    return factor

print(factor_counter(0))
print(factor_counter(3))
print(factor_counter(4))
print(factor_counter(200))


print('\n======================\n')

print("    Exercise 6")
# Output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None

def addition_table(given_number):
	iterated_number = 1
	my_sum = 1
	while iterated_number <= 5:    #limits the multiplier
		my_sum = given_number + iterated_number
		if my_sum > 20:    #limits the sum
			break
		print(str(given_number), "+", str(iterated_number), "=", str(my_sum))
		iterated_number += 1

addition_table(5)
addition_table(17)
addition_table(30)
