import time
import random

print('Welcome to self Time')
print()
print('The OBJ of the game is to not be a slow fuck')
print('A time will be displayed and it is your job to keep count')
print('Be the last one to sit and WIN!')

stand_time = random.randint(5, 20)

print('Stay standing for', stand_time, 'seconds.')

time.sleep(stand_time)

print('****TIME UP****')
