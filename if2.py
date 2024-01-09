bad_credit = False
good_credit = True
price = 1000000

if bad_credit:
    down_payment = price * 0.2
else:
    down_payment = price * 0.1
print(f'Down Payment: {down_payment}')


print("\n---------------------------------\n")


is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink Plenty of Water")
elif is_cold:
    print("It's a cold day")
    print("Bring a Sweater")
else:
    print('Normal Temperature Today')

print("Enjoy your day")
