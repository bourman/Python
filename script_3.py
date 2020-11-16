#script_3
while(True):
    choice = input("\nMenu:\n1.Print 100 numbers\n2.Check fiboo \n")
    if choice=="1":
        for i in range(101):
            print(i)
    elif choice=="2":
        fibo = [1, 2, 3, 5, 8, 13, 21]
        boolean = "True"
        for i in range(2, len(fibo)):
            print(fibo[i])
            print(fibo[i - 1])
            print(fibo[i - 2])
            print("\n")
            if fibo[i] == (fibo[i - 1] + fibo[i - 2]):
                continue
            else:
                boolean = "False"
                break
        if boolean == "True":
            print("It is fibo series")
        else:
            print("It isn't fibo series")
    else:
        print("\nEnter 1-2 only!!\n")
        continue
    if (input("Do you want to exit? y/n"))=="y":
        break
    else:
        print("Welcome back")
        continue
print("\nBye Bye...")
