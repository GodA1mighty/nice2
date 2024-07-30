fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]

while True:
    user_input = input("Enter the name of a fruit (type 'stop' to end): ")
    if user_input.lower() == 'stop':
        print("Program ended. Goodbye!")
        break

    if user_input in fruit_list:
        index = fruit_list.index(user_input)
        print(f"{user_input} is at index {index} in the list.")
    else:
        print(f"{user_input} is not in the list. Please try again.")