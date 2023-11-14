import matplotlib.pyplot as plt
import numpy as np

'Ecuacion 1'
# Define la función f(x, y) para la EDO
def edo1(x, y):
    return (4*x*y+1)/(3*(x**2))

def solucion_exacta(x):
    return -1.8*(x**(4/3))-1/(7*x)

#Funcion para el metodo de euler
def Euler_ampliado(a, b, y0, f, n):
    h = (b - a)/n
    x = a
    y = y0
    z = y0
    x_aprox = [x]
    y_aprox = [y]
    for i in range(0, n):
        
        z = y + h*f(x, y)
        y = y + h*(f(x, y) + f(x+h, z))/2
        x = x + h
        

        y_aprox.append(y)
        x_aprox.append(x)
    return x_aprox, y_aprox


def error_absoluto(solucion_exacta, x_numerico, y_numerico):
    # Calcula el valor de la solución exacta en los puntos numéricos
    y_exacto = [solucion_exacta(xi) for xi in x_numerico]

    # Calcula el error absoluto en cada punto
    error_abs = [abs(yn - ye) for yn, ye in zip(y_numerico, y_exacto)]

    return error_abs



#Pedimos por pantalla los extremos del intervalo
extremo_inf = float(input("Ingrese el extremo inferior del intervalo: "))
extremo_sup = float(input("Ingrese el extremo superior del intervalo: "))
N = 100 #Asumimos un numero de 100 intervalos

#Condiciones iniciales de la primera edo
y0_range = [-1]  # Condiciones iniciales para y
x0_range = [0.5]  # Condiciones iniciales para x

#Con este bucle mostramos la grafica
for i in range(len(y0_range)):
    y0 = y0_range[i]
    x0 = x0_range[i]
    x, y = Euler_ampliado(x0, extremo_sup, y0, edo1, N)
    plt.plot(x, y, label="Solución Aproximada con y0 = " + str(y0))
error = error_absoluto(solucion_exacta, x, y)
print("Error absoluto para y0 = " + str(y0) + ": " + str(error[-1]))



plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=1) #Eje x
plt.axvline(0, color='black', linewidth=1) #Eje y
plt.title("Solución de la EDO1 con el Método de Euler Ampliado")
plt.legend()
plt.grid(True)
plt.show()

