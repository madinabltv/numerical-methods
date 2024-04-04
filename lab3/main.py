import numpy as np

def fi(x):
    return 5.0

def analytic_func(x):
    return np.exp(4.0 * x) / 4.0 + np.exp(3.0 * x) / 3.0 + 5.0 / 12.0

def solve(pi, qi, a, b, n):
    h = 1.0 / n

    # Вычисление пар (xi, yi)
    xy = [(i * h, analytic_func(i * h)) for i in range(n + 1)]

    # Числа диагональной матрицы
    ai = 1.0 - (h / 2.0) * pi
    bi = h**2 * qi - 2.0
    ci = 1.0 + (h / 2.0) * pi

    # Вычисление массива d для метода прогонки
    d_res = [h**2 * fi(xy[i][0]) for i in range(n)]
    d_res[1] -= a * ai
    d_res[n-1] -= b * ci

    # Метод прогонки
    alpha = np.zeros(n)
    betta = np.zeros(n)

    y = bi
    alpha[1] = -ci / y
    betta[1] = d_res[1] / y

    for i in range(2, n):
        y = bi + ai * alpha[i - 1]
        alpha[i] = -ci / y
        betta[i] = (d_res[i] - ai * betta[i - 1]) / y

    # Обратный ход метода прогонки
    y_ch = np.zeros(n + 1)
    y_ch[0] = a
    y_ch[n-1] = betta[n-1]
    y_ch[n] = b
    for i in range(n - 2, 0, -1):
        y_ch[i] = alpha[i] * y_ch[i + 1] + betta[i]

    return xy, y_ch

def main():
    pi = -7.0
    qi = 12.0
    a = analytic_func(0.0)
    b = analytic_func(1.0)
    n = 10
     # вывести относительную погрещность в отчете

    xy, y_ch = solve(pi, qi, a, b, n)

    pogr = max(abs(xy[i][1] - y_ch[i]) / y_ch[i] for i in range(n))

    print("y''-7y'+12y = 5 ")
    print("   x        Analytic Solution     Numerical Solution     Relative Error")
    for i in range(n + 1):
        print(f"{xy[i][0]:.6f}        {xy[i][1]:.6f}              {y_ch[i]:.6f}           {(abs(xy[i][1] - y_ch[i]) / y_ch[i]):.6f}")

    print(f"Максимальная относительная погрешность: {pogr:.6f}")


main()
