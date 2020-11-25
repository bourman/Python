#!/bin/python3
#
def menu():
    while(True):
        choice=input("Enter your choice: \n1)Search url \n2)Add url+ip address \n3)Delete url \n4)Update ip address \n5)Print all ")
        if choice=="1":
            first()
        elif choice=="2":
            second()
        elif choice=="3":
            third()
        elif choice=="4":
            fourth()
        elif choice=="5":
            fifth()
        else:
            print("\n----------\nEnter 1-5 only!!!\n----------\n")
            continue
        if (input("Do you want to exit? yes/no") == "yes"):
            break
    print("Good bye!!!!1")



def first():
    look_url=input("Enter an url: ")
    if (look_url in dict):
        print("This url exists!")
    else:
        print("This url isn't exists!")


def second():
    print("Add another url and ip: ")
    dict.update({input("Add new url"): input("Add new ip address")})
    print("Adding the url and ip... ")
    print(dict)

def third():
    del_url=input("Enter the url you want to delete: ")
    dict.pop(del_url)
    print(dict)

def fourth():
    update_ip=input("Enter a new ip: ")
    current_url=input("Enter an exist url: ")
    dict.update({(current_url):(update_ip)})
    print(dict)


def fifth():
    print(dict)





dict={}
for i in range(6):
    dict.update({input("Add url"):input("Add ip address")})
    print(dict)
menu()
