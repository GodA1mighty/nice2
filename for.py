names = ['jason', 'jew', 'jon']
for name in names:
    print(f"hi {name}!")

print()

total = 0
for price in [10, 20, 30]:
    total += price
print(f"Total: {total}")

print()

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)