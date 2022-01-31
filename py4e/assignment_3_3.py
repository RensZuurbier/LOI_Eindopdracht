score = input("Enter a score between 0.0 and 1.0: ")

score = float(score)
if score > 1.0:
    print("This is above 1.0")
    quit()
elif score < 0.0:
    print("This is less than 0.0")
    quit()

if score < 0.6:
    print("F")
elif score < 0.7:
    print("D")
elif score < 0.8:
    print("C")
elif score < 0.9:
    print("B")
else:
    print ("A")
