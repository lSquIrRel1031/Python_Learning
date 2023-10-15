user_input = ''  # create the variable for the user input
inputs = []  # create the list to store the values
while user_input.lower() != "done":
    if user_input:
        inputs.append(user_input)

    user_input = input("'Enter a new value, or done when done'")
    print(inputs)