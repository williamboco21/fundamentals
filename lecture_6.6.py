# Finding the average in a loop

count = 0
the_sum = 0
print(f"Before average is {the_sum} and count is {count}")
for num in [9, 41, 74, 15, 3, 12]:
    count = count + 1
    the_sum = the_sum + num
    print(count, the_sum, num)

print(f"After average is {the_sum / count}")
