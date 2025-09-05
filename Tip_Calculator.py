print("Welcome to the tip Calculator! ")
bill=float(input("What was the total bill..? "))
tip=int(input("What percentage tip would you like to give? 10 12 15 "))
people=int(input("How many people to split the bill? "))
a=(bill*(tip/100))+bill
b=a/people
print("Each person Should Pay :",b  )
