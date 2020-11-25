#!/bin/python3

print("Enter your feet:\n----------")
feet=int(input("Your feet: "))
inch=int(input("Your inch: "))
inch+=feet * 12
cm=round(inch * 2.54)
print("Your height is: %d cm." % cm )
