# Summing in a loop

total = 0
print(f"Before total is {total}.")
for num in [9, 41, 74, 3,  15, 12]:
    total = total + num
    print(f"{total}, {num}")
print(f"After total is {total}")
