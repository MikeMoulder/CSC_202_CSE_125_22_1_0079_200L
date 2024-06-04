#Tip Calculator

print("Tip Calculator")
bill =  float(input("How much is the total bill? "))
tip = float(input("How much would you love to give as tip? "))

total = bill + tip
people =  int(input("How many people are paying? "))
amount = round(total/people, 2)
print(f"You have a bill of ${bill} and you are giving a tip of ${tip},"
+ f"also {people} people are paying, i.e each person will be paying ${amount}")