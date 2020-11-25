#!/bin/python3
#
ef menu(list_ip):
    while(True):
        choice=input("Enter your choice: \n1)Create new file \n2)Add new ip \n3)Remove specific IP \n4)Search specific IP \n5)Print all IP ")
        if choice=="1":
            create_file()
        elif choice=="2":
            list_ip=add_ip(list_ip)
        elif choice=="4":
            search_ip(list_ip)
        else:
            print("\n----------\nEnter 1-6 only!!!\n----------\n")
            continue
        if (input("Do you want to exit? y/n") == "y"):
            break
    print("Good bye !!!")


def create_file():
    print("Creating new file... ")


def add_ip(list_ip):
    new_ip=search_ip(list_ip)
    if(new_ip!=False):
        print("Adding new ip...")
        list_ip.append(new_ip)
        print("Your new  list of ips: " + str(list_ip))
        return list_ip

def search_ip(list_ip):
    new_ip=input("Enter ip: ")
    print("Searching... ")
    if(new_ip in list_ip):
        print("This ip is already in use!")
        return False
    else:
        print("This ip is available")
        return new_ip




my_list=["192.168.1.1","1.1.1.1","55.55.55.55"]
menu(my_list)
