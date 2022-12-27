from math import *

""" Заданные функции """
def testp(x):
    return 0

def testq(x):
    return -1

def testf(x):
    return -1

def p(x):
    return 2

def q(x):
    return -1/x

def f(x):
    return 3

""" Реализация алгоритма """
def alg(p, q, f, x0, xn, r1, s1, t1, r2, s2, t2, n):
    res = []
    h = (xn - x0) / n
    alpha = [0 for _ in range(n + 1)]
    alpha[1] = - (s1 / (h * r1 - s1))
    beta = [0 for _ in range(n + 1)]
    beta[1] = t1 / (r1 - s1 / h)
    x = [0 for _ in range(n + 1)]
    x[0] = x0
    x[n] = xn
    y = [0 for _ in range(n + 1)]
    for i in range(1, n):
        x[i] = x[i - 1] + h
        k1 = 1 / h ** 2 - p(x[i]) / (2 * h)
        k2 = 1 / h ** 2 + p(x[i]) / (2 * h)
        k3 = -2 / h ** 2 + q(x[i])
        alpha[i + 1] = -k2 / (k1 * alpha[i] + k3)
        beta[i + 1] = (f(x[i]) - k1 * beta[i]) / (k1 * alpha[i] + k3)
    tmp1 = s2 * beta[n] + t2 * h
    tmp2 = s2 * (1 - alpha[n]) + r2 * h
    y[n] = tmp1 / tmp2
    for i in range(n, 0, -1):
        y[i - 1] = y[i] * alpha[i] + beta[i]
    for i in range(n + 1):
        res.append((x[i], y[i]))
    return res

""" Выполнение программы """
def main():
    print(" --- testf 4 ---")
    res = alg(testp, testq, testf, -1, 1, 1, 0, 0, 1, 0, 0, 4)
    lenr = len(res)
    for i in range(lenr):
        print('%.6f' % res[i][0] + ' ' + '%.6f' % res[i][1], end="")
        if i < lenr - 1:
            print()
    print()
    
    print(" --- testf 25 ---")
    res = alg(testp, testq, testf, -1, 1, 1, 0, 0, 1, 0, 0, 25)
    lenr = len(res)
    for i in range(lenr):
        print('%.6f' % res[i][0] + ' ' + '%.6f' % res[i][1], end="")
        if i < lenr - 1:
            print()
    print()
    
    print(" --- testf 50 ---")
    res = alg(testp, testq, testf, -1, 1, 1, 0, 0, 1, 0, 0, 50)
    lenr = len(res)
    for i in range(lenr):
        print('%.6f' % res[i][0] + ' ' + '%.6f' % res[i][1], end="")
        if i < lenr - 1:
            print()
    print()
            
    print(" --- f 50 ---")
    res = alg(p, q, f, 0.2, 0.5, 1, 0, 1, 0.5, -1, 1, 50)
    lenr = len(res)
    for i in range(lenr):
        print('%.6f' % res[i][0] + ' ' + '%.6f' % res[i][1], end="")
        if i < lenr - 1:
            print()
    print()
            


main()
