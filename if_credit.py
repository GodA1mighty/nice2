bad_credit = False
good_credit = True
price = 1000000

if bad_credit:
    down_payment = price * 0.2
else:
    down_payment = price * 0.1
print(f'Down Payment: {down_payment}')
