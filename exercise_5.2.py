smallest = None
largest = None

while True:
    number = input("Enter a number: ")
    if number.lower() == 'done':
        break

    try:
        number = int(number)
    except:
        print("\nPlease enter a valid number.")
        continue

    if smallest is None and largest is None:
        largest = number
        smallest = number
    else:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

print(f"\nMaximum is {largest}.")
print(f"Minimum is {smallest}.")
