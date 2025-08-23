accuracy=int(input("Enter accuracy: "))
if accuracy>=0 and accuracy<=100:
    if accuracy>=90:
        print("Excellent Model")
    elif accuracy>=70 and accuracy<90:
        print("Good Model")
    elif accuracy>=50 and accuracy<70:
        print("Average Model")
    else:
        print("Poor Model")