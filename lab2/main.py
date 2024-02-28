# madina_bltv

def func(x):
    return x * (x ** 0.5) + 16

def spline(i, x, xi, a_coef, b_coef, c_coef, d_coef):
    return a_coef[i] + b_coef[i] * (x - xi[i]) + c_coef[i] * ((x - xi[i]) ** 2) + d_coef[i] *( (x - xi[i]) ** 3)

def main():
    from_val = 0
    to_val = 3
    n = 10
    h = (to_val - from_val) / n

    curx = from_val
    yi = [0 for k in range(0, n+1)]
    i = 0

    while (curx <= to_val):
        yi[i] = (curx * ((curx) ** 0.5) + 16)
        curx += h
        i += 1

    xi = [0 for k in range(0, n+1)]
    curx = from_val
    i = 0

    while (curx <= to_val):
        xi[i] = curx
        curx += h
        i += 1
        
    a_coef = [0 for k in range(0, n+1)]
    b_coef = [0 for k in range(0, n+1)]
    c_coef = [0 for k in range(0, n+1)]
    d_coef = [0 for k in range(0, n+1)]
    d_res = [0 for k in range(0, n+1)]
    for i in range(0, n):
        d_res[i] = (yi[i+1] - 2 * yi[i] + yi[i-1]) / (h * h)


    alpha = [0 for k in range(n)]
    beta = [0 for k in range(n)]
    y = 4

    alpha[1] = - 1 / y
    beta[1] = d_res[1] / y

    for i in range(2, n):
        y = 4 + 1 * alpha[i - 1]
        alpha[i] = -1 / y
        beta[i] = (d_res[i] - 1 * beta[i - 1]) / y

    c_coef[0] = 0
    c_coef[n] = 0
    c_coef[n-1] = beta[n-1]
    for i in range(n-2, 0, -1):
        c_coef[i] = alpha[i] * c_coef[i+1] + beta[i]

    for i in range(0, n-1):
        a_coef[i] = yi[i]
        b_coef[i] = ((yi[i+1] - yi[i]) / h) - (h / 3) * (c_coef[i+1] + 2 * c_coef[i])
        d_coef[i] = (c_coef[i+1] - c_coef[i]) / (3 * h)
    a_coef[n-1] = yi[n-1]
    b_coef[n-1] = ((yi[n] - yi[n-1]) / h) - (2 * h / 3) * c_coef[n-1]
    d_coef[n-1] = - c_coef[n] / (3 * h)

    print('x         S(x)      y(x)        |S(x) - y(x)| ')
    for i in range(0, n):
        y = func(xi[i])
        spl1 = spline(i, xi[i], xi, a_coef, b_coef, c_coef, d_coef)
        diff = abs(spl1 - y)
        
        print(f"{xi[i]:-2.5f}  {spl1:-10.5f}  {y:-10.5f} {diff:-10.5f}")
        
    print()
    print('(x[i]+x[i+1])/2   S(x)      y(x)      |S(x) - y(x)| ')

    for i in range(0, n):
        nel = (xi[i] +xi[i+1]) / 2
        spl = spline(i, nel, xi, a_coef, b_coef, c_coef, d_coef)
        y = func(nel)
        diff2 = abs(spl - y)        
            
        print(f"{nel:-2.5f}        {spl:-10.5f} {y:-10.5f} {diff2:-10.5f}")
main()
