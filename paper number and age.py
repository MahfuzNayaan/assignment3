age=int(input("Enter age :  "))
number_of_papers=int(input("Number of published papers :  "))
if age>=18:
    if number_of_papers>=2:
        print("Eligible to talk")
    else:
        print("Eligible to attend only")
else:
    print("Not eligible")