while True:
    try:
        number = int(input("Enter a positive number: "))

        if number > 0:
            print("Valid number:", number)
            break
        else:
            print("Number must be positive.")

    except ValueError:
        print("Please enter a valid number.")