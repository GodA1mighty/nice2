def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")

hint_username("je")


print(======================================)


def even_checker(number):
    if int(number) % 2 == 0:
        return True
    return False

print(even_checker("6"))


print(======================================)


"username to be more than 3 characters and less than 5 characters. also add and else statement that returns false"
def character_limit(username):
    if len(username) < 4:
        print('too short')
    elif len(username) > 4:
        print('too long')
    else:
        print("good to go")
character_limit('co1')


print(======================================)


prompt = 'perfect'
def character_limit(username):
    if len(username) < 4:
        short = 'too short'
    elif len(username) > 4:
        long = 'too long'        
    else:
        return prompt
character_limit('co1')


print(======================================)


def translate_error_code(error_code):
    if error_code == "401 Unauthorized":
        translation = "Server received an unauthenticated request"
    elif error_code == "404 Not Found":
        translation = "Requested web page not found on server"
    else:
        translation = "Unknown error code"
        return translation

print(translate_error_code("penis"))


print(======================================)


def round_up(number):
    x = 10
    whole_number = number // x
    print(whole_number)
    remainder = number % x
    print(remainder)
    if remainder >= 5:
        return x*(whole_number+1)
    return x*whole_number

print(round_up(35)) # Should print 40


print(======================================)


def task_reminder(time_as_string):
    if time_as_string == "8am":
        task = "Check overnight backup images"
    elif time_as_string == "11am":
        task = "Run TPS report"
    elif time_as_string == "5pm":
        task = "Reboot servers"
    else:
        task = "Provide IT Support to employees"
    return task

print(task_reminder("10am"))