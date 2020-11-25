#!/bin/python3
def menu(ip_add):
    while(True):
        choice=input("Enter your choice:\n1)Search specific IP \n@)Delete specific IP \n3)Add new IP \n4)Print specific IP \n5)Print all IP ")
        if choice=="1":
            first()
        elif choice=="2":
            second(ip_add)
        elif choice=="3":
            third(ip_add)
        elif choice=="4":
            fourth(ip_add)
        elif choice=="5":
            fifth(ip_add)
        else:
            print("\n----------\nEnter 1-5 only!!!\n----------\n")
            continue
        if (input("Do you want to exit? y/n") == "y"):
            break
    print("Good bye..")


def first(ip_add):
    search_ip=input("Search an ip: ")
    if (search_ip in ip_add):
        print ("This ip exist!")
        return False
    else:
        ("This ip isn't exist!")
        return search_ip
def second(ip_add):
    ip=first(ip_add)
    if(ip==False):
        print("Deleting the ip... ")
        ip_add=ip_add.remove(ip)
        print("The new list: " + str(ip_add))
    else:
        print("This ip doesnt exist...")


def third(ip_add):
    add_ip= first(ip_add)
    if(add_ip!=False):
        print("Adding new ip!")
        ip_add.append(add_ip)
        print(ip_add)

def fourth():
    spec_ip=int(input("Enter IP in the list that you want to see acorrding to his order:  "))
    print(ip_add[spec_ip-1])

def fifth():
    print(ip_add)






ip_add=[]
for i in range(6):
    ip_add.append(input("Enter ip: "))
    print(ip_add)
menu(ip_add)
