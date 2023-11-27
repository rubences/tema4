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
x, iteraciones = biseccion(a, b, tol)
print(f'Raíz aproximada: {x}')
print(f'Iteraciones: {iteraciones}')
x, iteraciones = secante(a, b, tol)
print(f'Raíz aproximada: {x}')
print(f'Iteraciones: {iteraciones}')
x, iteraciones = newton_raphson(a, tol)
print(f'Raíz aproximada: {x}')
print(f'Iteraciones: {iteraciones}')

import matplotlib.pyplot as plt

# Calcular las raíces e iteraciones
raiz_biseccion, iteraciones_biseccion = biseccion(a, b, tol)
raiz_secante, iteraciones_secante = secante(a, b, tol)
raiz_newton, iteraciones_newton = newton_raphson(a, tol)

# Crear una lista con los nombres de los métodos
metodos = ['Bisección', 'Secante', 'Newton-Raphson']

# Crear una lista con las iteraciones de cada método
iteraciones = [iteraciones_biseccion, iteraciones_secante, iteraciones_newton]

# Crear una gráfica de barras
plt.bar(metodos, iteraciones)
plt.xlabel('Método')
plt.ylabel('Iteraciones')
plt.title('Comparación de iteraciones para cada método')
plt.show()

# Path: ejercicio5.py