shopping_list = []

while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. Show list")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "added.")

    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed.")
        else:
            print("Item not found.")

    elif choice == "3":
        print("Shopping List:", shopping_list)

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")