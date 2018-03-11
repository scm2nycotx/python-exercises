#7. Tip Calculator
totalBillAmount = float(input("Total bill amout? "))
serviceLevel = input("Level of service? Good, fair, or bad?").lower()
if serviceLevel == "good":
    tipAmount = totalBillAmount * 0.2
    print("Tip amount: {}".format(round(tipAmount, 2)))
elif serviceLevel == "fair":
    tipAmount = totalBillAmount * 0.15
    print("Tip amount: {}".format(round(tipAmount, 2)))
else:
    tipAmount = totalBillAmount * 0.1
    print("Tip amount: {}".format(round(tipAmount, 2)))
totalAmount = totalBillAmount + tipAmount
print("Total amount: {}".format(round(totalAmount, 2)))

