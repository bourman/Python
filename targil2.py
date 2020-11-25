#!/bin/python3

number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
number3=int(input("Enter the third number: "))
sum=number1+number2+number3
if (number1 ==  number2 == number3):
    sum1=sum*3
    print("Your total value is " + str(sum1))
else:
    print("Your total value is " + str(sum))
