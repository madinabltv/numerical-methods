A = [[2, -1, 0],
     [5, 4, 2],
     [0, 1, -3]]

d = [3, 6, 2]

def find_x(A, d):
    n = len(A)
    x = [0 for k in range(0, n)]

    alpha = [0 for k in range(0, n)]
    beta = [0 for k in range(0, n)]
    Y = [0 for k in range(0, n)]

    Y[0] = A[0][0]
    alpha[0] = - A[0][1] / Y[0]
    beta[0] = d[0] / Y[0]

    for i in range(1,n-1):
        Y[i] = A[i][i] + A[i][i-1] * alpha[i-1]
        alpha[i] = - A[i][i+1] / Y[i]
        beta[i] = (d[i]-A[i][i-1] * beta[i-1]) / Y[i]

    Y[n-1] = A[n-1][n-1] + A[n-1][n-2] * alpha[n-2]
    beta[n-1] = (d[n-1] - A[n-1][n-2] * beta[n-2]) / Y[n-1]

    # print(Y)
    # print(alpha)
    # print(beta)

    x[n-1] = beta[n-1]
    for i in range(n-1, 0, -1):
        x[i-1] = alpha[i-1] * x[i] + beta[i-1]
    print(x)

find_x(A, d)

