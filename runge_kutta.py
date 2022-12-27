from math import *

""" Заданные функции """
def f(x, y):
    return (x - x ** 2) * y

def f1(x, u, v):
    return cos(u + 1.1 * v) + 2.1

def f2(x, u, v):
    return 1.1 / (x + 2.1 * u**2) + x + 1

""" Алгоритм Рунге-Кутта 2-ого порядка точности (для уравнения) """
def runge_kutt_eq_2(func, h, n, x, y):
    h = h / n
    for i in range(n):
        print(x, y)
        y += (func(x, y) + func(x + h, y + h * func(x, y))) * h / 2
        x += h
    print(x, y)
    

""" Алгоритм Рунге-Кутта 4-ого порядка точности (для уравнения) """
def runge_kutt_eq_4(func, h, n, x, y):
    h = h / n
    for i in range(n):
        print(x, y)
        k1 = func(x, y)
        k2 = func(x + h / 2, y + h / 2 * k1)
        k3 = func(x + h / 2, y + h / 2 * k2)
        k4 = func(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
    print(x, y)

""" Алгоритм Рунге-Кутта 2-ого порядка точности (для системы) """
def runge_kutt_sys_2(funcs, h, n, x, y):
    h = h / n
    syslen = 2
    for i in range(n):
        #print(x, y[0])
        print(x, y[1])
        tmp1 = [0] * syslen
        tmp2 = [0] * syslen
        for j in range(syslen):
            tmp1[j] = funcs[j](x, y[0], y[1])
            tmp2[j] = funcs[j](x + h, y[0] + h * tmp1[j], y[1] + h * tmp1[j])
        for j in range(syslen):
            y[j] += (tmp1[j] + tmp2[j]) * h / 2
        x += h
    #print(x, y[0])
    print(x, y[1])

""" Алгоритм Рунге-Кутта 4-ого порядка точности (для системы) """
def runge_kutt_sys_4(funcs, h, n, x, y):
    h = h / n
    syslen = 2
    for i in range(n):
        #print(x, y[0])
        print(x, y[1])
        k1 = [0] * syslen
        k2 = [0] * syslen
        k3 = [0] * syslen
        k4 = [0] * syslen
        for j in range(syslen):
            k1[j] = funcs[j](x, y[0], y[1])
        for j in range(syslen):
            k2[j] = funcs[j](x + h / 2, y[0] + h / 2 * k1[0], y[1] + h / 2 * k1[1])
        for j in range(syslen):
            k3[j] = funcs[j](x + h / 2, y[0] + h / 2 * k2[0], y[1] + h / 2 * k2[1])
        for j in range(syslen):
            k4[j] = funcs[j](x + h, y[0] + h * k3[0], y[1] + h * k3[1])
        for j in range(syslen):
            y[j] += h / 6 * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j])
        x += h
    #print(x, y[0])
    print(x, y[1])

""" Выполнение программы """
def test_eq():
    print("Проверка ДУ")
    n = 5
    print("    n =", n)
    print(" --- 2 порядок точности ---")
    runge_kutt_eq_2(f, 1, n, 0, 1)
    print(" --- 4 порядок точности ---")
    runge_kutt_eq_4(f, 1, n, 0, 1)
    print()
    
    n = 25
    print("    n =", n)
    print(" --- 2 порядок точности ---")
    runge_kutt_eq_2(f, 1, n, 0, 1)
    print(" --- 4 порядок точности ---")
    runge_kutt_eq_4(f, 1, n, 0, 1)
    print()
    
    n = 50
    print("    n =", n)
    print(" --- 2 порядок точности ---")
    runge_kutt_eq_2(f, 1, n, 0, 1)
    print(" --- 4 порядок точности ---")
    runge_kutt_eq_4(f, 1, n, 0, 1)

def test_sys():
    print("Проверка СДУ")
    n = 5
    print("    n =", n)
    print(" --- 2 порядок точности ---")
    runge_kutt_sys_2([f1, f2], 1, n, 0, [1, 0.05])
    print(" --- 4 порядок точности ---")
    runge_kutt_sys_4([f1, f2], 1, n, 0, [1, 0.05])
    print()
    
    n = 25
    print("    n =", n)
    print(" --- 2 порядок точности ---")
    runge_kutt_sys_2([f1, f2], 1, n, 0, [1, 0.05])
    print(" --- 4 порядок точности ---")
    runge_kutt_sys_4([f1, f2], 1, n, 0, [1, 0.05])
    print()
    
    n = 50
    print("    n =", n)
    print(" --- 2 порядок точности ---")
    runge_kutt_sys_2([f1, f2], 1, n, 0, [1, 0.05])
    print(" --- 4 порядок точности ---")
    runge_kutt_sys_4([f1, f2], 1, n, 0, [1, 0.05])

def main():
    test_sys()


main()