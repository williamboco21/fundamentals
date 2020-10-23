count = 0
total = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        number = float(number)
    except:
        print("Invalid input")
        continue

    count = count + 1
    total = total + int(number)


print(total, count, total / count)