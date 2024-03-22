                #Structure:
            #Recursion
# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print("Factorial of 5 is:", result)

#you can add an input wby replacing the following:
# x = input("Here: ")
# result = factorial(int(x))
# print("Factorial of " + (x) + " is:", result)


#In the context of factorial(5), the recursion unfolds as follows:
# factorial(5) calls factorial(4) since n * factorial(n - 1) is 5 * factorial(4).
# factorial(4) calls factorial(3) since n * factorial(n - 1) is 4 * factorial(3).
# This pattern continues until factorial(1) is called, which returns 1.
# Then, factorial(2) returns 2 * factorial(1), which is 2 * 1 = 2.

# factorial(3) returns 3 * factorial(2), which is 3 * 2 = 6.
# factorial(4) returns 4 * factorial(3), which is 4 * 6 = 24.
# Finally, factorial(5) returns 5 * factorial(4), which is 5 * 24 = 120.

print("\n==============\n")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(6)
print("Fibonacci number at position 6 is:", result)


print("\n==============\n")


def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

result = reverse_string("hello")
print("Reversed string:", result)


print("\n==============\n")


def sum_list(arr):
    if not arr:
        return 0
    else:
        return arr[0] + sum_list(arr[1:])

result = sum_list([1, 2, 3, 4, 5])
print("Sum of numbers in the list:", result)


print("\n==============\n")


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

factorial(30)
#recursion are limited up to 1000


print("\n==============\n")


def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4)
