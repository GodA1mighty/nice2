for item in 'Python': #each letter printed on it's own line
    print(item)
```````````````````````````````    
for item in ['Mosh', 'John', 'Sarah']: #prints each string on it's own line
    print(item)
```````````````````````````````
for item in [1, 2, 3, 4]: #prints numbers on it's own line
    print(item)
```````````````````````````````
for item in range(10): #prints numbers on it's own line using range
    print(item)
```````````````````````````````
for item in range(5, 10, 2): #prints numbers on it's own line using the range
    print(item)              #while skipping the list by 2
```````````````````````````````
#shopping cart
total = 0
for price in [10, 20, 30]:
    total += price
print(f"Total: {total}")
