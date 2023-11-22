names = ['prince', 'bama', 'shaq']
names.sort() #sort() is a method, names is a var
print(names)

#reverse alphabet
print('--------line6--------')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #reverse being an argument
print(cars)

print('--------line11--------')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) #keeps original order of list but prints in alphabetical order. could add the "reverse=True" arguement as well
print("\nHere is the original list again:")
print(cars)

print('--------------line20--------------')
#Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #reverses in chronological order, not alphabetical order
print(cars)

print('--------------line27--------------')
#length
cars = ['bmw','audi','toyota','subaru']
print(len(cars))