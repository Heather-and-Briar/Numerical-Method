""" ������� ���������� ��������� ������� ������� n """
def identity_matrix(n):
    i_matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            if i == j:
                line.append(1)
            else:
                line.append(0)
        i_matrix.append(line)
    return i_matrix

""" ���� ���� (������� A � ������� b) �� ����� - ���������� 1-2 """
def get_system_from_file(path):
    with open(path, "r") as file:
        n = int(file.readline())    # ������� ������� A
        a = []    # ������� A
        b = []    # ������ b
        for line in file:
            ln = list(map(float, line.split()))
            tmp = [ln.pop(-1)]
            b.append(tmp)
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
        b.append([linefunc(i)])
    return n, a, b

""" ���� ���� (������� A � ������� b) �� ������������ ������ ����� """
def get_system_from_stdin():
    n = int(input())    # ������� ������� A
    a = []    # ������� A
    b = []    # ������ b
    for i in range(n):
        line = list(map(float, input().split()))
        tmp = [line.pop(-1)]
        b.append(tmp)
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
            print(b[i][0], end=', ')
        else:
            print(b[i][0], end='')
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

""" ���������� ����������� ����� ������ """
def matrix_norm(matrix):
    res = 0
    for i in range(len(matrix)):
        tmp = 0
        for j in range(len(matrix[0])):
            tmp += abs(matrix[i][j])
        if tmp > res:
            res = tmp
    return res

""" ���������� ����� ��������������� ������� """
def conditional_number(matrix, method, det):
    return matrix_norm(matrix) * matrix_norm(inverse_matrix(matrix, method, det))

""" ���������� �������� ������� """
def inverse_matrix(matrix, method, det):
    mtrx = method(augmented_matrix(matrix, identity_matrix(len(matrix))), det)
    res = get_answer(mtrx)
    return res

""" ������� ���������� ����������� ������� """
def augmented_matrix(matrix1, matrix2):
    res = []
    for i in range(len(matrix1)):
        res.append(matrix1[i] + matrix2[i])
    return res

""" ������� ��������� �� ����������� ������� ����� (������ ��� ������� ����/������� ��� ������ �������� �������) """
def get_answer(matrix):
    if matrix == -1:
        return -1
    
    ans = []
    ln = len(matrix)
    for i in range(ln):
        line = []
        for j in range(ln, len(matrix[0])):
            line.append(matrix[i][j])
        ans.append(line)
    return ans

""" ������������ �������������� ������� ������� """
def swap_lines(matrix, i, j):    # ������� ������ i-�� � j-�� ������ �������
    matrix[i], matrix[j] = matrix[j], matrix[i]

def mul_line(matrix, i, num):    # ������� �������� i-�� ������ ������� �� ����� num
    for j in range(len(matrix[0])):
        matrix[i][j] *= num

def add_lines(matrix, i1, i2, coef):    # ������� ��������� � i1-�� ������ i2-�� � ������������� coef
    for j in range(len(matrix[0])):
        matrix[i1][j] += coef * matrix[i2][j]

""" ����� ������ """
""" � ����������� �� ����������� ������� (������� A + ������-������� b/��������� �������) ��������� ���� ������� ����, ���� �������� ������� """
def gauss_method(matrix, det):
    n = len(matrix)
    swap_counter = 0
    det[0] = 1

    # ������ ���

    for j in range(n):
        for i in range(j, n):
            if matrix[i][j] != 0:
                swap_lines(matrix, j, i)
                swap_counter += 1
                break
        
        det[0] *= matrix[j][j]
        if matrix[j][j] == 0:
            print("\n������� - ���������. ��� ������������ �������")
            return -1

        mul_line(matrix, j, 1 / matrix[j][j])
        for i in range(j + 1, n):
            coef = -matrix[i][j]
            add_lines(matrix, i, j, coef)

    det[0] *= (-1) ** (swap_counter % 2)

    # �������� ���

    for j in range(n - 1, -1, -1):
        mul_line(matrix, j, 1 / matrix[j][j])
        for i in range(j - 1, -1, -1):
            coef = -matrix[i][j]
            add_lines(matrix, i, j, coef)
    return matrix

""" ����� ������ � ������� �������� �������� """
""" � ����������� �� ����������� ������� (������� A + ������-������� b/��������� �������) ��������� ���� ������� ����, ���� �������� ������� """
def modified_gauss_method(matrix, det):
    n = len(matrix)
    swap_counter = 0
    det[0] = 1

    # ������ ���

    for j in range(n):
        leading_elem = abs(matrix[j][j])
        leading_elem_num = j
        for i in range(j, n):
            cur_elem = abs(matrix[i][j])
            if cur_elem > leading_elem:
                leading_elem = cur_elem
                leading_elem_num = i
        swap_counter += 1
        swap_lines(matrix, j, leading_elem_num)

        det[0] *= matrix[j][j]
        if matrix[j][j] == 0:
            print("\n������� - ���������. ��� ������������ �������")
            return -1

        mul_line(matrix, j, 1 / matrix[j][j])
        for i in range(j + 1, n):
            coef = -matrix[i][j]
            add_lines(matrix, i, j, coef)

    det[0] *= (-1) ** (swap_counter % 2)

    # �������� ���

    for j in range(n - 1, -1, -1):
        mul_line(matrix, j, 1 / matrix[j][j])
        for i in range(j - 1, -1, -1):
            coef = -matrix[i][j]
            add_lines(matrix, i, j, coef)

    return matrix

""" ���������� ��������� """
def main():
    print("����� �������� ������ ���� (A*x = b)?")
    print("    1 - �� ����� (��. ���������� 1-2)")
    print("    2 - ������������� (��. ���������� 2 (�. 1-6))")
    print("    3 - �� ������������ ������ �����")
    method = int(input())
    if method == 1:
        print("������� ����� �������: 1, 2 ��� 3")
        method = int(input())
        if method == 1:
            n, a, b = get_system_from_file('gauss1.txt')
        elif method == 2:
            n, a, b = get_system_from_file('gauss2.txt')
        elif method == 3:
            n, a, b = get_system_from_file('gauss3.txt')
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
    
    det = [10]    # ������������ �������
    
    print("����� ������� ������ ����?")
    print("    1 - ������� ������")
    print("    2 - ���������������� ������� ������")
    method = int(input())
    if method == 1:
        gauss = gauss_method
    elif method == 2:
        gauss = modified_gauss_method
    else:
        print("�������� ����� ������")
        return
        
    ans = get_answer(gauss(augmented_matrix(a, b), det))
    if ans == -1:
        return
    
    print("\n�����:")
    print_vector(ans)
    print()
    
    print("\n������������ ������� A =", det[0])
    print()
    
    print("�������� � A �������:")
    print_matrix(inverse_matrix(a, gauss, det))
    print()
    
    print("����� ��������������� ������� A =", conditional_number(a, gauss, det))
    

main()