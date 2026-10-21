#PROBLEM 2
import numpy as np
import matplotlib.pyplot as plt
# Gradiant descent  (Xnew = Xold  - (learning rate * gradient))
def f(x):
     return x**2 + 3*x + 4
def df(x):
    return 2*x + 3 
x = 9
learning_rate = 0.1
iteratons = 5

history = [x]
for i in range(iteratons):
   grad = df(x)
   x = x- learning_rate * grad
   history.append(x)

   print("iteratons:", i+1)
   print("Grad:", grad)
   print("x =", x)
   print("f(x) =", f(x)) 
   print("-----------------")
x_value = np.linspace(-16, 15, 100)
y_value = f(x_value)
plt.figure(figsize=(10,6))

plt.plot(x_value, y_value, linewidth=3, label="Function")

plt.plot(history, [f(i) for i in history], "r--")

plt.scatter(history, [f(i) for i in history], s=70, color="red", label="Descent Path")
plt.scatter(history[0], f(history[0]), s=120, color="green", label="Start") # s means dots
plt.scatter(-1.5, f(-1.5), marker="*", s=250, color="gold", label="Minimum")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Finding the minimum using Gradient Descent")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
