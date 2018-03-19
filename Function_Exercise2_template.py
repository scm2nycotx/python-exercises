import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot

def f(x):
    return x + 1
x_list = list(range(-3, 4))
f_output = []
for x in x_list:
    f_output.append(f(x))

plot.plot(x_list, f_output)
plot.show()
# the above method doesn't work, it still does not show the output. 
# it seems to be a backend issue.
# but I used the following code, still didn't work
# import matplotlib
# matplotlib.get_backend()
# 'Qt4Agg'




