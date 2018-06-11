'''An example python script to explain the difference
between running python on notebooks and via the command line'''

##import certain functions from modules
from example_module import polynomial
from numpy import arange
##Here, we import the matplotlib.pyplot class and name it plt
import matplotlib.pyplot as plt


def third_order_polynomial(x,a=1,b=1,c=1,d=0):
    '''Returns the 3rd order polynomial of x,
    using the coefficients a,b,c as
    a*x**3 + b*x**2 + c*x + d'''
    return a*x**3 + b*x**2 + c*x + d

##If running as main programme, do this
if __name__ == "__main__":
    ##Create some x_values
    x_values = arange(-10.,10,0.1)
    
    ##Plot 2nd order polynomial and label it '2nd order'
    plt.plot(x_values,polynomial(x_values),label='2nd order')
    ##Plot 3rd order polynomial and label it '3rd order'
    plt.plot(x_values,third_order_polynomial(x_values),label='3rd order')
    ##This command adds a legend to the plot
    plt.legend()
    ##Once created, open the plot
    plt.show()