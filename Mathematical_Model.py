import numpy as np

x = np.array([8,6,15,20,25,11,5,32,28,20])
y = np.array([15,20,20,40,50,25,10,55,35,30])

n = len(x)

x_bar = np.sum(x) / n
y_bar = np.sum(y) / n

numerador = np.sum((x - x_bar)*(y - y_bar))
denominador = np.sum((x - x_bar)**2)

b = numerador / denominador
a = y_bar - b*x_bar

y_modelo = a + b*x
erro = y - y_modelo
