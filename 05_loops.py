numbers = [12, 7, 25, 4, 18, 9, 30]

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)