loss=float(input("Enter initial loss: "))
subtract=0.05
while loss>0.1:
    print("current loss",loss)
    loss=loss-subtract
print("Final loss: ",loss)