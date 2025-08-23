problem_type=input("Enter problem type: ")
dataset_size=int(input("Enter data set size: "))
if problem_type=="classification":
    if dataset_size<=5000:
        print("Logistic regression")
    else:
        print("Neuraln network")
if problem_type=="regression":
    if dataset_size<=10000:
        print("Linear Regression")
    else:
        print("XGBoost")