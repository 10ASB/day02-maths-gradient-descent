##Gradiant decent 3
from email import iterators
import numpy as np
def f(x,y):
    return x**2 + y**2
def dfx(x):
    return 2*x
def dfy(y):
    return 2*y
#initalising value 
x = 6
y = 7
learning_rate = 1.5 # 0.001 slow , 0.01 slow n stable , 0.5 fast, 1.5 over for mini
iterators = 5

## gradiant desent 
for i in range(iterators):
    grad_x = dfx(x)
    grad_y = dfy(y)

    x = x - learning_rate * grad_x
    y = y - learning_rate * grad_y

    print(f"iteraton{i+1}")
    print(f"x = {x:.4f}")
    print(f"y = {y:.4f}")
    print(f"f(x,y) = {f(x,y):.4f}")
    print("///////////////////////")
