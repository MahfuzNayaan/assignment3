password=input("Enter a password: ").upper()
if len(password)>=8:
    if "AI" in password:
        print("Strong password")
    else:
        print("Weak password")
else:
    print("Invalid password")