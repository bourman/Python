#!/bin/python3
#
budget=int(input("Enter your total budget(Dollar): "))
facebook=int(input("How long facebook campagin will run? "))
instagram=int(input("How long intagram campagin will run? "))
sum=((facebook*100) + (instagram*50))
#sum2=(int(sum*1.17*3.5))
print("\nSum with fee: " + str(sum) + " $")
#print("\nSum with fee: " + str("%.1f" % (sum*1.17*3.5)) + " NIS")
if (budget >= sum):
    print("Successfull and you have got: " + str(budget-sum) + " $")
else:
    print("The price is too expensive you have to add: " + str(sum-budget) + " $")
