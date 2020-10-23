# Finding the largest number

largest_number = -1
print("Before, the largest is", largest_number)
for thing in [9, 41, 12, 3, 74, 15]:
    if thing > largest_number:
        largest_number = thing
    print(largest_number, thing)
print("The largest number is", largest_number) 
