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






