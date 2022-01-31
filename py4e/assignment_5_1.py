largest_number = None
smallest_number = None

while True :
    number = input('Enter a number: ')
    if number == 'done' :
        print('Maximum is',int(largest_number))
        print('Minimum is',int(smallest_number))
        break
    try:
        number = float(number)
    except:
        print('Invalid input')
        continue
    if largest_number is None :
        largest_number = number
    elif largest_number < number :
        largest_number = number

    if smallest_number is None :
        smallest_number = number
    elif smallest_number > number :
        smallest_number = number
