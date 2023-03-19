#This code demonstrates the Collatz Conjecture computationally
#if a%2==0: means if a is even
import matplotlib.pyplot as plt
import numpy as np
n=int(input('Please enter a positive integer'))


#n=987
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
end=input("")