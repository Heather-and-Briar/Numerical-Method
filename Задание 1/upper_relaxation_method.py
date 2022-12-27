from copy import deepcopy

""" Ввод СЛАУ (матрицы A и вектора b) из файла - приложение 1-2 """
def get_system_from_file(path):
    with open(path, "r") as file:
        n = int(file.readline())
        a = []    # матрица A
        b = []    # вектор b
        for line in file:
            ln = list(map(float, line.split()))
            b.append(ln.pop(-1))
            a.append(ln)
    return n, a, b

""" Генерация СЛАУ (матрицы A и вектора b) с помощью функций - приложение 2 (пример 1-6) """
def generate_matrix_element(i, j, n=25, m=10):    # функции для генерации элемента [i, j] матрицы A
    if i != j:
        return (i + j) / (m + n)
    return n + m ** 2 + j / m + i / n

def generate_vector_element(i, n=25):    # функция для генерации элемента [i] вектора b
    return i ** 2 - n

def get_system_by_generation(matrfunc, linefunc, n=25):
    a = []    # матрица A
    b = []    # вектор b
    for i in range(n):
        line = []
        for j in range(n):
            line.append(matrfunc(i, j))
        a.append(line)
    for i in range(n):
        b.append(linefunc(i))
    return n, a, b

""" Ввод СЛАУ (матрицы A и вектора b) со стандартного потока ввода """
def get_system_from_stdin():
    n = int(input())
    a = []    # матрица A
    b = []    # вектор b
    for i in range(n):
        line = list(map(float, input().split()))
        b.append(line.pop(-1))
        a.append(line)
    return n, a, b


""" Вывод матрицы """
def print_matrix(matrix):
    if matrix == -1:
        return
    for i in range(len(matrix)):
        print(*matrix[i])

""" Вывод СЛАУ (матрицы A и вектора b) для WolframAlpha """
def print_wolfram_matrix(matrix):    # вывод матрицы
    if matrix == -1:
        return
    print('(', end='')
    n = len(matrix)
    for i in range(n):
        if i < n - 1:
            print(tuple(matrix[i]), end=', ')
        else:
            print(tuple(matrix[i]), end='')
    print(')', end='')

def print_vector(b):    # вывод вектора
    print('(', end='')
    n = len(b)
    for i in range(n):
        if i < n - 1:
            print(b[i], end=', ')
        else:
            print(b[i], end='')
    print(')', end='')

def print_wolfram(matrix, b):
    print('solve(', end='')
    print_wolfram_matrix(matrix)
    print('*(', end='')
    n = len(matrix)
    for i in range(n):
        if i < n - 1:
            print('x' + str(i + 1), ', ', end='')
        else:
            print('x' + str(i + 1), end='')
    print(')=', end='')
    print_vector(b)
    print(', (', end='')
    for i in range(n):
        if i < n - 1:
            print('x' + str(i + 1), ', ', end='')
        else:
            print('x' + str(i + 1), end='')
    print('))', end='')

""" Вычисление нормы для условия окончания метода верхней релаксации """
def norm(v1, v2):
    res = 0
    n = len(v1)
    for i in range(n):
        res += abs(v1[i] - v2[i])
    return res

""" Метод верхней релаксации """
""" (Метод Зейделя - частный случай метода верхней релаксации при w = 1) """
def upper_relaxation_method(a, b, eps, w):
    n = len(a)
    cur_x = [0 for _ in range(n)]
    prev_x = [0 for _ in range(n)]
    iterations = 0
    flag = True    # цикл должен выполниться хотя бы 1 раз
    while norm(cur_x, prev_x) > eps or flag:
        prev_x = deepcopy(cur_x)
        for i in range(n):
            tmp = 0
            for j in range(i):
                tmp += a[i][j] * cur_x[j]
            for j in range(i, n):
                tmp += a[i][j] * prev_x[j]
            cur_x[i] = prev_x[i] + w * (b[i] - tmp) / a[i][i]
        iterations += 1
        if iterations > 100000:
            print("Матрица не является положительно определённой")
            return -1, iterations
        flag = False
    for i in range(len(cur_x)):
        cur_x[i] = int(cur_x[i] * 100000000) /100000000
    return cur_x, iterations

""" Выполнение программы """
def main():
    print("Каким способом ввести СЛАУ (A*x = b)?")
    print("    1 - из файла")
    print("    2 - сгенерировать (см. приложение 2 (п. 1-6))")
    print("    3 - со стандартного потока ввода")
    method = int(input())
    if method == 1:
        print("Введите номер системы: 1, 2 или 3")
        method = int(input())
        if method == 1:
            n, a, b = get_system_from_file('relax1.txt')
        elif method == 2:
            n, a, b = get_system_from_file('relax2.txt')
        elif method == 3:
            n, a, b = get_system_from_file('relax3.txt')
        else:
            print("Неверный номер системы")
            return
    elif method == 2:
        n, a, b = get_system_by_generation(generate_matrix_element, generate_vector_element)
    elif method == 3:
        print("Вводите СЛАУ в формате:")
        print("n")
        print("a11 a12 ... a1n b1")
        print("a21 a22 ... a2n b2")
        print("...")
        print("an1 an2 ... ann bn")
        n, a, b = get_system_from_stdin()
    else:
        print("Неверный номер способа")
        return
        
    print("Порядок матрицы A:", n)
    print()
        
    print("Матрица A:")
    print_matrix(a)
    print()
        
    print("Вектор b:")
    print_vector(b)
    print()
   
    print()
    print("Матрица и СЛАУ в формате для проверки в WolframAlpha")
    print_wolfram_matrix(a)
    print()
    print_wolfram(a, b)
    print()
    print()
   
    print("\nОтвет, полученный методом Зейделя:")
    ans, iterations = upper_relaxation_method(a, b, 0.0000001, 1)
    if a == -1:
        return
    print_vector(ans)
    print()
    print("    Кол-во итераций ", iterations)
    print()

    w = 0.1
    for i in range(1, 19):
        if (i == 10):
            w += 0.1
            continue
        print("\nОтвет, полученный методом верхней релаксации ( w =", w, "):")
        ans, iterations = upper_relaxation_method(a, b, 0.0000001, w)
        print_vector(ans)
        print()
        print("    Кол-во итераций ", iterations)
        print()
        w += 0.1


main()
