hours = input("Enter hours: ")
rate = input("Enter rate: ")

ihours = float(hours)
irate = float(rate)

# Calculate the hours above 40
extra_hours = 0
while ihours > 40:
    ihours = ihours -1
    extra_hours = extra_hours + 1

# Calculate the pay including the bonus rate
bonus_rate = irate * 1.5
pay = ihours * irate + extra_hours * bonus_rate

print(pay)
