print('-----original-----')
places = ['athens','petra','alaska','moon','sweden']
print(places)

print('-----Sorted-----')
print(sorted(places))
print(places)

print('-----Reverse-----')
places.reverse()
print(places)
places.reverse()
print(places)

print('-----Sort-----')
places.sort()
print(places)

print('-----SortedReverse-----')
a = sorted(places)
a.sort(reverse=True)
print(a)
print(places)