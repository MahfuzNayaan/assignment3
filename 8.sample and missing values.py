samples=int(input("Enter number of sample: " ))
missing=int(input("Enter missing rate: "))
if samples>=1000:
    if missing<=10:
        print("Good Dataset")
    else:
        print("Needs Cleaning")
else:
    print("Insufficient Data")