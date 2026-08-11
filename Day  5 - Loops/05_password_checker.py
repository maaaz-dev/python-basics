correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Login successful!")
        break

    attempts -= 1
    print("Wrong password.")
    print("Attempts left:", attempts)

if attempts == 0:
    print("Account locked.")