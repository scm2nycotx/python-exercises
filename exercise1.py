# 1. Hello, you!
name = input("What is your name?")
print("Hello, {}!!".format(name))

# 2. HELLO, YOU!
name = input("What is your name?".upper())
print("Hello, {}!!".format(name).upper())
print("Your name has {} letters in it! Awesome!!".format(len(name)).upper())

# 3. Madlib
print("Please fill in the blanks below:")
print("________'s favorite subject in school is ________.")
name = input("What is name?")
subject = input("What is subject?")
print("{0}'s favorite subject in school is {1}".format(name, subject))

#4. Day of the Week
day = int(input("Day (0-6)? "))
list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print("Today is",list[day],"!")

#5. Work or Sleep In?
day = int(input("Day (0-6)? "))
if day > 5 or day < 1:
    print("Great, sleep in!")
else:
    print("Go to work!")
    
#6. Celsius to Fahrenheit
AnsInC = int(input("Temperature in C?"))
F = AnsInC * 1.8 + 32
print(F, "F")

#7. Tip Calculator
totalBillAmount = float(input("Total bill amout? "))
serviceLevel = input("Level of service? Good, fair, or bad? ").lower()
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

#8. Tip Calculator 2
totalBillAmount = float(input("Total bill amount? "))
serviceLevel = input("Level of service? Good, fair, or bad? ").lower()
splitWays = input("Split how many ways? ")
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
amountPerPerson = totalAmount / int(splitWays) 
print("Amount per person: {}".format(round(amountPerPerson, 2)))

#9. 1 to 10
count = 0
while count < 10:
  count += 1
  print("The count is: ", count)

#10. How many coins?
print("You have 0 coins now.")
count = 0
while True:
    answer = input("Do you want another? ")
    if answer.lower() == "yes":
       count += 1
       print("You have {} coins".format(count))
    if answer.lower() == "no":
       count += 1
       break
print("See you next time!")
        
    

    
  





