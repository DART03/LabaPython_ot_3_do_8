
#лабораторная 3 работа 3
from math import exp

print('Вычисление e^x с помощью ряда Тейлора (Лаб. работа №3, Задание 3)')
xb = float(input('Xbeg = '))
xe = float(input('Xend = '))
dx = float(input('Dx = '))
eps = float(input('Eps = '))

print("+---------+------------+-------+")
print("|    X    |     Y      |   N   |")
print("+---------+------------+-------+")

xt = xb
while xt <= xe:
    an = 1.0
    s = an
    n = 0
    while True:
        n += 1
        an = an * xt / n
        s += an
        if abs(an) < eps:
            break
    print(f"| {xt:7.2f} | {s:10.3f} | {n:5d} |")
    xt += dx
print("+---------+------------+-------+")
