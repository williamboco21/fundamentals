def computepay(hours, rate):
    base_hour = 40

    if hours > base_hour:
        base_pay = base_hour * rate
        overtime_pay = (hours - base_hour) * rate * 1.5
        pay = base_pay + overtime_pay
    else:
        pay = base_hour * rate

    return pay


try:
    hrs = float(input("Enter the number of hours: "))
    rate_per_hour = float(input("Enter the rate: "))
except:
    print("Error, please enter a number.")
    quit()

pay = computepay(hrs, rate_per_hour)
print("Pay", pay)