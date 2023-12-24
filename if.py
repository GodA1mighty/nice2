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

print()

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

print()

#use of parentheses ()
high_income2 = False
good_credit2 = True
student2 = False
if (high_income2 or good_credit2) and not student2:
    print("3Eligible")
else:
    print("3Not Eligible")

print()

age2 = 22
if age2 >= 18 and age2 < 65:
#or expressed like:
#if 18 <= age < 65:
    print("Eligible4")

print()

g = 9
h = 8
if g < h:
	print('g is less than h')
else:
	if g == h:
		print('g is equal to h')
	else:
		print('g is greater than h')