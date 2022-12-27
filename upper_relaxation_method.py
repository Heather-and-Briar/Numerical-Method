from copy import deepcopy

""" ���� ���� (������� A � ������� b) �� ����� - ���������� 1-2 """
def get_system_from_file(path):
    with open(path, "r") as file:
        n = int(file.readline())
        a = []    # ������� A
        b = []    # ������ b
        for line in file:
            ln = list(map(float, line.split()))
            b.append(ln.pop(-1))
            a.append(ln)
    return n, a, b

""" ��������� ���� (������� A � ������� b) � ������� ������� - ���������� 2 (������ 1-6) """
def generate_matrix_element(i, j, n=25, m=10):    # ������� ��� ��������� �������� [i, j] ������� A
    if i != j:
        return (i + j) / (m + n)
    return n + m ** 2 + j / m + i / n

def generate_vector_element(i, n=25):    # ������� ��� ��������� �������� [i] ������� b
    return i ** 2 - n

def get_system_by_generation(matrfunc, linefunc, n=25):
    a = []    # ������� A
    b = []    # ������ b
    for i in range(n):
        line = []
        for j in range(n):
            line.append(matrfunc(i, j))
        a.append(line)
    for i in range(n):
        b.append(linefunc(i))
    return n, a, b

""" ���� ���� (������� A � ������� b) �� ������������ ������ ����� """
def get_system_from_stdin():
    n = int(input())
    a = []    # ������� A
    b = []    # ������ b
    for i in range(n):
        line = list(map(float, input().split()))
        b.append(line.pop(-1))
        a.append(line)
    return n, a, b


""" ����� ������� """
def print_matrix(matrix):
    if matrix == -1:
        return
    for i in range(len(matrix)):
        print(*matrix[i])

""" ����� ���� (������� A � ������� b) ��� WolframAlpha """
def print_wolfram_matrix(matrix):    # ����� �������
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

def print_vector(b):    # ����� �������
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

""" ���������� ����� ��� ������� ��������� ������ ������� ���������� """
def norm(v1, v2):
    res = 0
    n = len(v1)
    for i in range(n):
        res += abs(v1[i] - v2[i])
    return res

""" ����� ������� ���������� """
""" (����� ������� - ������� ������ ������ ������� ���������� ��� w = 1) """
def upper_relaxation_method(a, b, eps, w):
    n = len(a)
    cur_x = [0 for _ in range(n)]
    prev_x = [0 for _ in range(n)]
    iterations = 0
    flag = True    # ���� ������ ����������� ���� �� 1 ���
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
            print("������� �� �������� ������������ �����������")
            return -1, iterations
        flag = False
    for i in range(len(cur_x)):
        cur_x[i] = int(cur_x[i] * 100000000) /100000000
    return cur_x, iterations

""" ���������� ��������� """
def main():
    print("����� �������� ������ ���� (A*x = b)?")
    print("    1 - �� �����")
    print("    2 - ������������� (��. ���������� 2 (�. 1-6))")
    print("    3 - �� ������������ ������ �����")
    method = int(input())
    if method == 1:
        print("������� ����� �������: 1, 2 ��� 3")
        method = int(input())
        if method == 1:
            n, a, b = get_system_from_file('relax1.txt')
        elif method == 2:
            n, a, b = get_system_from_file('relax2.txt')
        elif method == 3:
            n, a, b = get_system_from_file('relax3.txt')
        else:
            print("�������� ����� �������")
            return
    elif method == 2:
        n, a, b = get_system_by_generation(generate_matrix_element, generate_vector_element)
    elif method == 3:
        print("������� ���� � �������:")
        print("n")
        print("a11 a12 ... a1n b1")
        print("a21 a22 ... a2n b2")
        print("...")
        print("an1 an2 ... ann bn")
        n, a, b = get_system_from_stdin()
    else:
        print("�������� ����� �������")
        return
        
    print("������� ������� A:", n)
    print()
        
    print("������� A:")
    print_matrix(a)
    print()
        
    print("������ b:")
    print_vector(b)
    print()
   
    print()
    print("������� � ���� � ������� ��� �������� � WolframAlpha")
    print_wolfram_matrix(a)
    print()
    print_wolfram(a, b)
    print()
    print()
   
    print("\n�����, ���������� ������� �������:")
    ans, iterations = upper_relaxation_method(a, b, 0.0000001, 1)
    if a == -1:
        return
    print_vector(ans)
    print()
    print("    ���-�� �������� ", iterations)
    print()

    w = 0.1
    for i in range(1, 19):
        if (i == 10):
            w += 0.1
            continue
        print("\n�����, ���������� ������� ������� ���������� ( w =", w, "):")
        ans, iterations = upper_relaxation_method(a, b, 0.0000001, w)
        print_vector(ans)
        print()
        print("    ���-�� �������� ", iterations)
        print()
        w += 0.1


main()