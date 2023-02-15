import math
import numpy as np
import scipy. stats as stats
import matplotlib.pyplot as plt
from scipy import integrate

a = 45 #k = 8
b = 6000 #o = 65

n = 500

#случайная величина
def X(n):
    x = []
    for i in range(n):
        x.append(i)
    return x

#плотность распределения
def f(t):
    a = 45
    b = 6000
    if (t >= a and t <= b):
        f = (2/(b - a) - 2/math.pow((b - a), 2))*math.fabs(a + b - 2*t) # f = math.pow(t, k - 1) * (math.exp(-t/o)/(math.pow(o, k)*math.factorial(k))
    else:
        f = 0
    return f

#вероятность распределения
def V():
    for i in range(n + 1):
        x = [i for i in range(n)]
        y = [f(i) for i in range(n)]

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f")
    plt.title('Плотность вероятности')
    plt.show()

def Integral(n):
    sum = 0
    for i in range(1, n):
        sum += f(i)

    I = sum
    return I
def F():
    I = 0
    x = []
    y = []
    for i in range(1, n):
        x.append(i)
        y.append(Integral(i))

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("F")
    plt.title('Функция распределения')
    plt.show()

    return I

#метод прямоугольников
def integral(f):
    sum = 0
    for i in range(1, n + 1):
        sum += f

    I = sum / n
    return I

def Mf(t):
    c = (a + b) / 2
    if (t >= 0):
        f = t * (2/(b - a) - 2/math.pow((b - a), 2))*math.fabs(a + b - 2*t) # f = t * math.pow(t, k - 1) * (math.exp(-t/o)/(math.pow(o, k)*math.factorial(k))
    else:
        f = 0
    return f

def Mf_2(t):
    if (t >= 0):
        f = t * t * (2/(b - a) - 2/math.pow((b - a), 2))*math.fabs(a + b - 2*t) # f = t * t * math.pow(t, k - 1) * (math.exp(-t/o)/(math.pow(o, k)*math.factorial(k))
    else:
        f = 0
    return f

def M():
    M = 0
    h = 1
    i = 0
    while (i <= n):
        M += ((Mf(i) + Mf(i - 1)) * h) / 2
        i += h
    return M

def D():
    M2 = 0
    M = 0
    h = 1
    i = 0
    while (i <= n):
        M += ((Mf(i) + Mf(i - 1)) * h) / 2
        M2 += ((Mf_2(i) + Mf_2(i - 1)) * h) / 2
        i += h
        D = M2 - M ** 2
    return D

def C():
    C = math.sqrt(math.fabs(D()))
    return C

V()
F()
print('M = {0}'.format(M()))
print('D = {0}'.format(D()))
print('C = {0}'.format(C()))

#встроенный метод
print(stats.gamma.median(8, scale=65))
print(stats.gamma.var(8, scale=65))