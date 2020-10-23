# Finding the smallest value

smallest_number = None
print("Before, the smallest is", smallest_number)
for num in [9, 41, 12, 3, 74, 15]:

    # We set the first value as the smallest number
    if smallest_number is None:
        smallest_number = num
    elif num < smallest_number:
        smallest_number = num
    print(smallest_number, num)
print("The smallest number is", smallest_number)
