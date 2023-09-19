import time
time_text = input('Enter the alarm time in seconds: ')
time_int = int(time_text)
print('Alarm Set')
time.sleep(time_int)
print('Time is up')

#or

import time
time_int = int(input('Enter the alarm time in seconds: '))
print('Alarm Set')
time.sleep(time_int)
print('Time is up')
               
