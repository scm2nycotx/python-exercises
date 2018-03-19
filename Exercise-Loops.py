#1. 1 to 10
for number in range(1, 11):
    print(number)
    
#2. n to m
startNum = int(input("What number to start from? "))
endNum = int(input("What number to end on? "))
for number in range(startNum, endNum + 1):
    print(number)

#3. Odd Numbers
for number in range(1, 11):
    if number % 2 == 1:
        print(number)
        
#4. Print a Square
def solidSquare(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print("*", end=" ") 
        print()
solidSquare(5, 5)

#5. Print a Square II
def solidSquare2(N, M):
    for i in range(1, N + 1):
        for j in range(1, M +1):
            print("*", end=" ")
        print()
sizeOfSquare = int(input("How big is the square? "))
solidSquare2(sizeOfSquare, sizeOfSquare)

#6. Print a Box
def box(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 or i == n or j == 1 or j == m):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
width = int(input("What is the width? "))
height = int(input("What is the height? "))
box(height, width)

#7. Print a Triangle (failed)
def triangle(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 and j == 4):
                print("*", end=" ")
            elif (i == 2 and 5 >= j >= 3):
                print("*", end=" ")
            elif (i == 3 and 6 >= j >= 2):
                print("*", end=" ")
            elif (i == 4 and 7 >= j >= 1):
                print("*", end=" ")
        print()
        
triangle(4, 7)

#7b. (worked)
def pyramid(height):
    for k in range(1, height + 1):
        rows = (height - (k - 1)) * " " + (k - 1) * "*" + "*" + (k - 1) * "*"
        print (rows)

pyramid(4)

#8. Print a Triangle II
#For exemple, we set the height = 8, then just call the function with k = 8

pyramid(8)

#9. Multiplication Table
numFrom = int(input("Enter your number from? "))
numTo = int(input("Enter your number to? "))
limit = int(input("Enter your limit? "))
for a in range(numFrom, numTo + 1):
    for b in range(1, limit + 1):
        print("{}  X {:2} = {:2}".format(a, b, a * b))
        
#10. Print a Banner
text = input("Any words to say? ")
print("*" * 28)
print("*" + " " + text + " " + "*")
print("*" * 28)

#11. Triangle Numbers
def triangularNum(n):
    for i in range(1, n + 1):
        y = i * (i + 1) / 2
        print(y)

triangularNum(10)

#12. Factor a Number
def factorsOfNum(x):
    print("The factors of " + str(x) + " are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
num = int(input("Enter a number, I will show you its factors: "))

factorsOfNum(num)



            
    






























    

