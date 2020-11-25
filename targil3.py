#!/bin/python3
#targil_3
number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
sum=number1+number2
if sum in range(15,20):
    print("Your total value is 20" )
else:
    print("Your total value is " + str(sum))
