# Step 1
print("I am thinking of a number between 1 and 10.")
secret_number = 5
while True:
    answer = int(input("What is the number of your guess? "))
    if answer == secret_number:
       print("Yes! You Win!!")
       break
    else:
       print("Nope, try again!")
        
# Step 2: Give High-Low Hint
print("I am thinking of a number between 1 and 10.")
secret_number = 5
while True:
    answer = int(input("What is the number of your guess? "))
    if answer == secret_number:
       print("Yes! You Win!!")
       break
    elif answer > secret_number:
       print("{} is too high! Try a lower one!".format(answer))
    else:
       print("{} is too low! Try a higher one!".format(answer))
       
# Step 3: Randomly Generated Secret Number
import random
my_random_number = random.randint(1, 10)
print("A random number is generated between 1 and 10.")
while True:
    answer = int(input("What is the number of your guess? "))
    if answer == my_random_number:
       print("Yes! You got it!!")
       break
    elif answer > my_random_number:
       print("{} is too high! Try a lower one!".format(answer))
    else:
       print("{} is too low! Try a higher one!".format(answer))

# Step 4: Limit Number of Guesses
import random
my_random_number = random.randint(1, 10)
print("A random number is generated between 1 and 10.")
print("You have five guesses left.")
count = 5
while count > 0:
    answer = int(input("What is the number of your guess? "))
    if answer == my_random_number:
       print("Yes! You got it!!")
       break
    elif answer > my_random_number:
       print("{} is too high! Try a lower one!".format(answer))
       count -= 1
    else:
       print("{} is too low! Try a higher one!".format(answer))
       count -= 1
print("You ran out of guesses!")

# Bonus: Play Again
import random
def play():
    my_random_number = random.randint(1, 10)
    print("A random number is generated between 1 and 10.")
    print("You have five guesses left.")
    count = 5
    while count > 0:
        answer = int(input("What is the number of your guess? "))
        if answer == my_random_number:
            print("Yes! You got it!!")
            againOrnot = input("Do you want to play again (Yes or No)? ")
            if againOrnot.lower() == "yes":
                play()
            if againOrnot.lower() == "no":
                print("See you!")
        elif answer > my_random_number:
            print("{} is too high! Try a lower one!".format(answer))
            count -= 1
        else:
            print("{} is too low! Try a higher one!".format(answer))
            count -= 1
    print("You ran out of guesses!")
    againOrnot = input("Do you want to play again (Yes or No)? ")
    if againOrnot.lower() == "yes":
        play()
    if againOrnot.lower() == "no":
        print("See you!")
