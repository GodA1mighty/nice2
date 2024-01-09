import time

print(time.ctime(0))    #shows the time when your computer think was the beginning, turned into a string
print(time.time())    #returns current seconds since epoch (when your computer thinks time began)
print(time.ctime())    #shows the current datetime

print()

time_object = time.localtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)

print()

print(time.gmtime())    #UTC time

print()

#(year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

#amount of seconds since epoch
time_tuple2 = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple2)
print(time_string)


print("\n--------------------------------------------\n")


import time
print("What is the capital of the state of North Dakota?")
time.sleep(1)
print("Bismarck")
time.sleep(0.5)    #half a millisecond
print("Bismarck")


print("\n--------------------------------------------\n")


import time

my_time = int(input("Enter the time in seconds: "))
for x in range(0, my_time):
    time.sleep(1)
print("TIME'S UP!")


print("\n--------------------------------------------\n")


import time

my_time = int(input("Enter the time in seconds: "))
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME'S UP!")
