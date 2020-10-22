hours = float(input("Enter number of hours: "))
rate = float(input("Enter rate: "))
base_hour = 40
base_pay = base_hour * rate

if hours > 40:
    overtime_hours = hours - base_hour
    overtime_pay = (overtime_hours * rate) * 1.5
    pay = base_pay + overtime_pay

else:
    pay = base_pay

print(pay)