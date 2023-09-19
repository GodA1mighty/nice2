a = input('What is your credit score? ')
b = int(a)

price = 1000000
credit_good = round(int(price) * 1.1)
credit_bad = round(int(price) * 1.2)

if b<680:
    print('The Down Payment will be',credit_bad)
else:
    print('Your Down Payment will be',credit_good)
