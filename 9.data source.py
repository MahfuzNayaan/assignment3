data_source=input("Enter data source type: ")
consent=input("Enter consent: ")
if data_source=="public":
    print("Usable data")
else:
    if consent=="yes":
        print("Usable data")
    else:
        print("Ethical issue")