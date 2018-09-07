import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys as sy

msg="Hell World. We rock"
print(msg)

#x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
#plt.plot(x, np.sin(x))       # Plot the sine of each x point
#plt.show()                   # Display the plot

flag=True
if(flag):
    print "Success"

def fabonacci(n=10):
    a,b=0,1
    while a<n:
        print(a)
        a,b=b,a+b
    print()

fabonacci(100)