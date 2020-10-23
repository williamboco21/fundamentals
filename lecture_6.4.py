# Counting in a loop

count = 0
print(f"Before count is {count}.")
for num in [9, 41, 12, 74, 15]:
    count = count + 1
    print(f"{count}, {num}")
print(f"After count is {count}")
