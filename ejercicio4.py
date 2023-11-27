import math

def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

def biseccion(a, b, tol):
    iteraciones = 0
    while (b - a) / 2.0 > tol:
        iteraciones += 1
        c = (a + b) / 2.0
        if f(c) == 0:
            return c, iteraciones
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0, iteraciones

def secante(x0, x1, tol):
    iteraciones = 0
    while abs(x1 - x0) > tol:
        iteraciones += 1
        x0, x1 = x1, x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
    return x1, iteraciones

def newton_raphson(x0, tol):
    iteraciones = 0
    while True:
        iteraciones += 1
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol:
            return x1, iteraciones
        x0 = x1

# Programa principal
a, b = 1, 2
tol = 1e-6
print("Método de bisección:", biseccion(a, b, tol))
print("Método de la secante:", secante(a, b, tol))
print("Método de Newton-Raphson:", newton_raphson(a, tol))