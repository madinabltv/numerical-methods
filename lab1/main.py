import numpy as np

A = [[4, 1, 0, 0],
     [1, 4, 1, 0],
     [0, 1, 4, 1],
     [0, 0, 1, 4]]

d = [5, 6, 6, 5]
# необходимые и достаточные условия
def necessity(A):
    n = len(A)

    for i in range(1, n-1):
        if abs(A[i][i]) < abs(A[i][i+1]):
            print('Не выполнено условия диагонального преобладания 1')
            return False

    for i in range(1, n-1):
        if abs(A[i][i]) < abs(A[i-2][i-1]):
            print('Не выполнено условия диагонального преобладания 2')
            return False

    for i in range(1, n-1):
        if abs(A[i][i]) < abs(A[i-2][i-1]) + abs(A[i][i+1]):
            print('Не выполнено условия диагонального преобладания 3')
            return False

    for i in range(1, n-1):
        if A[i][i] == 0:
            print('Нулевые элементы на главной диагонали')
            return False
    return True

def find_x(A, d):
    n = len(A)

    if (not necessity(A)):
        print("Условия необходимости и достаточности не выполняются")
        return -1

    x = [0 for k in range(0, n)]

    alpha = [0 for k in range(0, n)]
    beta = [0 for k in range(0, n)]
    Y = [0 for k in range(0, n)]

    Y[0] = A[0][0]
    alpha[0] = - A[0][1] / Y[0]
    beta[0] = d[0] / Y[0]

    for i in range(1, n-1):
        Y[i] = A[i][i] + A[i][i-1]*alpha[i-1]
        alpha[i] = - A[i][i+1] / Y[i]
        beta[i] = (d[i]-A[i][i-1]*beta[i-1]) / Y[i]

    Y[n-1] = A[n-1][n-1] + A[n-1][n-2] * alpha[n-2]
    beta[n-1] = (d[n-1] - A[n-1][n-2] * beta[n-2]) / Y[n-1]

    # print(Y)
    # print(alpha)
    # print(beta)

    x[n-1] = beta[n-1]
    for i in range(n-1, 0, -1):
        x[i-1] = alpha[i-1] * x[i] + beta[i-1]

    for i in range(0, n):
        print(f'x[{i}] =', x[i])
    print()

    x1 = [1, 1, 1, 1]

    e = [0 for k in range(0, n)]

    for i in range(0, n):
        e[i] = x[i] - x1[i]
        print("Погрешность {:.20f}".format(e[i]))
    print(e)

# погрешность

    # d1 = [0 for k in range(0,n)]
    # for i in range(0,n):
    #     for j in range(0,n):
    #         d1[i] += A[i][j] * x[j]
    # # print(d1)
    # r = [0 for k in range(0, n)]
    # for i in range(0, n):
    #     r[i] = d[i] - d1[i]
    # e = [0 for k in range(0, n)]
    #
    # A_inv = np.linalg.inv(A)
    # # print(A_inv)
    #
    # for i in range(0, n):
    #     e[i] += A_inv[i][i] * r[i]
    #     print("Погрешность {:.20f}".format(e[i]))
    # print()
    #
    # for i in range(0, n):
    #     c = x[i] + e[i]
    #     print(f'Приближенное значение x[{i}] =', c)

find_x(A, d)
