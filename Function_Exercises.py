#1. Hello
def hello(name):
    print("Hello, {}".format(name))
hello("Chih-Ming Sun")

#2. y = x + 1
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot

def f(x):
    return x + 1
x_list = list(range(-3, 4))
f_output = []
for x in x_list:
    f_output.append(f(x))

print(x_list)
print(f_output)

pyplot.plot(x_list, f_output)
pyplot.savefig("function_ex2_plot.png")
pyplot.close()

#3. Square of x 
def f(x):
    return x * x
x_list = list(range(-100, 100))
f_output = []
for x in x_list:
    f_output.append(f(x))

pyplot.plot(x_list, f_output)
pyplot.savefig("function_ex3_plot.png")
pyplot.close()

#4. Odd or Even
def f(x):
    if x % 2 == 1:
        return 1
    else:
        return -1
        
x_list = list(range(-5, 6))
f_output = []
for x in x_list:
    f_output.append(f(x))

pyplot.bar(x_list, f_output)
pyplot.savefig("function_ex4_plot.png")
pyplot.close()

#5. Sine
import math
def f(x):
    return math.sin(x)
x_list = list(range(-5, 6))
f_output = []
for x in x_list:
    f_output.append(f(x))

pyplot.plot(x_list, f_output)
pyplot.savefig("function_ex5_plot.png")
pyplot.close()

#6. Sine 2
import matplotlib.pyplot as plot
import numpy as np

x = np.arange(-5, 6, 0.1)
y = np.sin(x)

plot.plot(x, y)
plot.title("Sine wave")
plot.xlabel("Time : x")
plot.ylabel("Amplitude : y = sin(x)")
plot.axhline(y = 0, color = "k")
plot.savefig("function_ex6_plot.png")
plot.close()

#7. Degree Conversion
# Celcius converts to Fahrenheit

x = np.arange(-100, 100, 1)
y = 1.8 * x + 32

plot.plot(x, y)
plot.title("Celcius to Fahrenheit conversion")
plot.xlabel("Celcius : x")
plot.ylabel("Fahrenheit : y = 1.8 * x + 32")
plot.axhline(y = 32, color = "black")
plot.axvline(x = 0, color = "black")
plot.savefig("function_ex7_plot.png")
plot.close()

#8. Play again?
def playAgain(x):
    answer = input("Do you want to play again (Y or N)? ")
    if answer == "Y":
        return True
    else:
        return False

playAgain(x)

#9. Play again? Again.
def playAgain2(x):
    answer2 = input("Do you want to play again (Y or N)? ")
    if answer2 == "Y":
        return True
    elif answer2 == "N":
        return False
    else:
        answer3 = input("Invalid input, try again (Y or N)? ")
        if answer3 == "Y":
            return True
        elif answer3 == "N":
            return False
            
playAgain2(x)




    

