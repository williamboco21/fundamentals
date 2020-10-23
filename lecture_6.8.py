# Using Boolean to search a number

found = False
print("Before", found)

for num in [9, 41, 15, 12, 3, 74]:
    if num == 3:
        found = True
        break 
    print(num, found)
print("After", found)