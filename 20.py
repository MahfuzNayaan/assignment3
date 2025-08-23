marks=int(input("Enter marks: "))
if marks>0 and marks <=100:
    if marks>=80:
        print("AI expert")
    elif  marks>=60:
        print("AI leraner")
    else:
        print("needs inprovment")
else:
    print("out of range")