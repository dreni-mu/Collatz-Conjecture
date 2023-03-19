#This code computes the Collatz Conjecture and plots the graph for the first 1000 positive integers
#if a%2==0: means if a is even
import matplotlib.pyplot as plt
import numpy as np


for n in range(1,1000):
    i=n
    y=[i]
    while n == n:
        if i==1:
            break
        if i%2==0:
            z=i/2
        else:
            z=(i*3)+1
        y.append(z)
        i=z
    print("for number",n,"graph:=")
    x=np.linspace(1,len(y),len(y))
    plt.plot(x,y)