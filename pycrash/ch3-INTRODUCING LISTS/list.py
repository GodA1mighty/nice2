bi = ['1', '7', '8', '3']
print(bi)
bi = ['yee', 'snap', 'boi', '3']
print(bi[0])
bi = ['yee', 'snap', 'boi', '3']
print(bi[0].title()) #caps the 1st letter
bi = ['yee', 'snap', 'boi', '3']
print(bi[-1])
print(bi[-2])

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati') #adds ducati to the end of the list
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati') #insert anywhere you place the index (in this case it is 1)
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[2] #when you want to delete an item from a list and not use that item in any way, use the del statement
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() #if you want to use an item as you remove it, use the pop() method.
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")