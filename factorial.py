def factorial(n):
    # variable for the answer
    fact = 1

    if n == 1 or n == 0:
        print(f"The factorial is {fact}.")
    else:
        for i in range(n, 0, -1):
            fact = fact * i

        print(f"The factorial of {n} is {fact}.")


num = int(input("Enter a number: "))

factorial(num)