smallest = None
largest = None

while True:
    number = input("Enter a number: ")
    if number == "done":
        break

    try:
        number = int(number)
    except:
        print("Invalid input")
        continue

    if smallest is None and largest is None:
        smallest = number
        largest = number
    else:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

print("Maximum is", largest)
print("Minimum is", smallest)
