#!/bin/python3
#
def menu():
    while(True):
        choice=input("Enter your choice: \n1)Search ip address \n2)Add ip address \n3)Delete ip address \n4)Print all the ip in the list ")
        if choice=="1":
            first()
        elif choice=="2":
            second()
        elif choice=="3":
            third()
        elif choice=="4":
            fourth()
        else:
            print("\n----------\nEnter 1-4 only!!!\n----------\n")
            continue
        if (input("Do you want to exit? yes/no") == "yes"):
            break
    print("Good bye !!")


def first():
    look_ip=input("Enter an ip: ")
    if (look_ip in ip_add):
        print("This ip exists!")
    else:
        print("This ip isn't exists!")

def second():
    new_ip=input("Add new ip address: ")
    ip_add.append(new_ip)
    print(ip_add)

def third():
    del_ip=input("Delete an ip address: ")
    ip_add.remove(del_ip)
    print(ip_add)

def fourth():
    print(ip_add)







ip_add=[]
for i in range(6):
    ip_add.append(input("Enter new ip: "))
    print(ip_add)
menu()
