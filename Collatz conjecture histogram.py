#This code computes the collatz conjecture for the first 1000 positive integers and records the frequency of each starting digit in a histogram
#If ran for enough iterations, this histogram will tend towards a distribution resembling Benford's Law :)
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(1,9,9)
y=np.zeros(9)
for n in range(1,1000):
    i=n*100
    while n == n:
        f_digit=int(str(i)[0])
        y[f_digit-1]=y[f_digit-1]+1
        print(y)
        if i==1:
            break
        if i%2==0:
            z=i/2
        else:
            z=(i*3)+1
        i=z
    plt.plot(x,y)
    plt.show()