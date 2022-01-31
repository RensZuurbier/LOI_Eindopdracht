friends = ["Axel", "Chiel", "Bono"]
for friend in friends :
  print("Happy national adolfday", friend)

nummers = [1,2,3,4,5,6,7,8,9]
for i in nummers:
    print(i)


## Finding the largest number
largest_so_far = -1
print("Largest number before the loop =", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, "vs", the_num)
print("Now the largest number is", largest_so_far)

## Finding the smallest number
smallest = None
print("Before loop, the smallest is",smallest)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif  value < smallest :
        smallest = value
    print(value, "smallest =",smallest)
print("After the loop, the smalles is", smallest)
