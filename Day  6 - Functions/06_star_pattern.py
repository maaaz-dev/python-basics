def print_stars(rows):
    for i in range(1, rows + 1):
        print("*" * i)


rows = int(input("Enter number of rows: "))

print_stars(rows)