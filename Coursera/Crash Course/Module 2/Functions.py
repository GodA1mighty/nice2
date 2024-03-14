#Functions
def greeting(name, department):
  print("Welcome, " + name)
  print("You are part of " + department)


greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering")

print()


def area_triangle(base, height):
  return base * height / 2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: ", sum)
#or
print("The sum of both areas is: " + str(sum))

print()
print('========================')
print()

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

print()

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)

print()

time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))
