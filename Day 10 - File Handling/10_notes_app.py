while True:
    print("\n1. Add Note")
    print("2. Read Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()

        print("Note saved.")

    elif choice == "2":
        file = open("notes.txt", "r")
        notes = file.read()
        file.close()

        print("\nYour Notes:")
        print(notes)

    elif choice == "3":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")