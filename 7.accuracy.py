accuracy=int(input("Enter accuracy: "))
latency=int(input("Enter latency: "))
if accuracy>=85:
    if latency<=100:
        print("Ready to Production")
    else:
        print("Needs optimization")
else:
    print("Not suitable for Deployment ")