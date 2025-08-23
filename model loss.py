model_1_loss=int(input("Enter loss value of model_1: "))
model_2_loss=int(input("Enter loss value of model_2: "))
if (model_1_loss >=0 and model_1_loss<=100) and(model_2_loss >=0 and model_2_loss<=100):

    if model_1_loss>model_2_loss:
        print("model_2 is better")
    elif model_2_loss>model_1_loss:
        print("model_1 is better")
    else:
        print("Both model are equal ")