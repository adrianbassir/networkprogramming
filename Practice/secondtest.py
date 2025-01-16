while True:
    try:
        user_input = -1
        user_input = int(input("Enter a number (-1 to stop): "))
        if user_input == -1:
            break
    except ValueError:
        print(f"{user_input} is not an integer")
