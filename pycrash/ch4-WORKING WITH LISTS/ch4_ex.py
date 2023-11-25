pizzas = ['pepperoni','cheese','italian',]
for pizza in pizzas:
    print(f"I like {pizza}!")
print('\nI really like pizza!')

print('\n-----line6-----')
for x in range(21):
    print(x)

print('\n-----line10-----')
numbers = list(range(1, 21))
print(numbers)

print('\n-----line14-----')
digits = list(range(1,1000001))
print(min(digits))
print(max(digits))
print(sum(digits))

print('\n-----line20-----')
numbers = list(range(1, 31, 3))
print(numbers)

print('\n-----line24-----')
square = [value**3 for value in range(1,11)]
print(square)

print('\n-----line28-----')
food = ['pizza','donuts','cake','chicken','sandwich']
print('The first three items in the list are:')
print(food[:3])

print('\n-----line33-----')
food = ['pizza','donuts','cake','chicken','sandwich']
print('Three items from the middle of the list are:')
print(food[1:4])

print('\n-----line38-----')
food = ['pizza','donuts','cake','chicken','sandwich']
print('The last three items in the list are:')
print(food[2:])

print('\n-----line43-----')
my_pizzas = ['pepperoni','chicken','pineapple','sausage','sardine']
friend_pizzas = my_pizzas[:]
my_pizzas.append('cheese')
friend_pizzas.append('bacon')
print("My favorite pizzas are:")
for m_pizza in my_pizzas:
    print(m_pizza)
print("My friend's favorite pizzas are:")
for f_pizza in friend_pizzas:
    print(f_pizza)
