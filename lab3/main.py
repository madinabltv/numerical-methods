import math
x = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
y = [3.93, 2.3, 1.6, 1.27, 1.18, 0.99, 1.41, 0.8, 1.12]
n = len(x)

 #  кубическая аппроксимация
def f(x):
    return -0.1040 * (x ** 3) +1.1970 * (x ** 2) - 4.53258 * x + 6.7550

x_a = (x[0] + x[n - 1]) / 2
x_g = (x[0] * x[n - 1]) ** 0.5
x_h = 2 / (1 / x[0] + 1 / x[n - 1])
# print(x_a, x_g, x_h)

y_a = (y[0] + y[n - 1]) / 2
y_g = (y[0] * y[n - 1]) ** 0.5
y_h = 2 / (1 / y[0] + 1 / y[n - 1])
# print(y_a, y_g, y_h)

z_a = f(x_a)
z_g = f(x_g)
z_h = f(x_h)
# print(z_a, z_g, z_h)

d1 = abs(z_a - y_a)
d2 = abs(z_g - y_g)
d3 = abs(z_a - y_g)
d4 = abs(z_g - y_a)
d5 = abs(z_h - y_a)
d6 = abs(z_a - y_h)
d7 = abs(z_h - y_h)
d8 = abs(z_h - y_g)
d9 = abs(z_g - y_h)
# d = min(d1, d2, d3, d4, d5, d6, d7, d8, d9)
# print(d)
# print(d1, d2, d3, d4, d5, d6, d7, d8, d9)

# минимальная дельта d8

def sum1():
    sum = 0
    for i in range(n):
        sum += (1 / x[i])
    return sum

def sum2():
    sum = 0
    for i in range(n):
        sum += math.log(y[i])
    return sum

def sum3():
    sum = 0
    for i in range(n):
        sum += (1 / x[i] ** 2)
    return sum

def sum4():
    sum = 0
    for i in range(n):
        sum += math.log(y[i]) / x[i]
    return sum

b = ((sum1() * sum2()) - sum4() * n) / (sum1() * sum1() - sum3() * n)
# print(b)
a = (sum4() - b * sum3()) / sum1()
# print(a)

a = math.e ** a
# print(a, b)

def z8(a, b, x):
    return a * math.e ** (b / x)

evasion = 0
for i in range(n):
    evasion += (z8(a, b, x[i]) - y[i]) ** 2
evasion = math.sqrt(evasion)
# print(evasion)

deviation = evasion / math.sqrt(n)
# print(deviation)
print('a = ', a)
print('b = ', b)
print('Среднеквадратичное уклонение', evasion)
print('Среднеквадратичное отклонение', deviation)
