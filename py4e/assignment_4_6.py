def computepay(hours, rate):
    if hours > 40:
        regular_hours = hours * rate
        overtime_hours = (hours -40) * (rate * 0.50)
        pay = regular_hours + overtime_hours
    else:
        pay = hours * rate
    return pay

hours = input("Enter hours: ")
hours = float(hours)

rate = input("Enter rate: ")
rate = float(rate)

pay = computepay(hours,rate)
print("Pay",pay)
