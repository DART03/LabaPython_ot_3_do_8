#Лабораторная работа 7 вариант 3 

import turtle as tr

def f_taylor_exp(x):
    # Вычисление e^x через ряд Тейлора для построения графика
    an = 1.0
    s = an
    n = 1
    while n < 20: # ограничим число итераций для графического построения
        an = an * x / n
        s += an
        n += 1
    return s

def draw_axes(aX, aY):
    # Рисование осей координат
    tr.up()
    # Ось X
    tr.goto(aX[0], 0)
    tr.down()
    tr.goto(aX[1], 0)
    
    # Ось Y
    tr.up()
    tr.goto(0, aY[0])
    tr.down()
    tr.goto(0, aY[1])

def main():
    # Настройка границ холста и мира (Вариант 3)
    aX = [-6, 6]
    aY = [-2, 20]
    
    tr.setup(800, 600)
    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])
    tr.title("Лабораторная работа №7 - Вариант 3 (Модуль turtle)")
    
    tr.speed(0)
    tr.width(2)
    tr.color("blue")
    
    # Рисуем оси
    draw_axes(aX, aY)
    
    # Рисуем график функции e^x
    tr.color("green")
    tr.width(3)
    
    dx = 0.1
    x = aX[0]
    
    # Поднимаем перо для первой точки
    y = f_taylor_exp(x)
    tr.up()
    tr.goto(x, y)
    tr.down()
    
    while x <= aX[1]:
        y = f_taylor_exp(x)
        # Защита от ухода графика слишком высоко за пределы экрана
        if aY[0] <= y <= aY[1]:
            tr.goto(x, y)
        else:
            tr.up()
        x += dx
        
    tr.ht()
    print("График успешно построен в окне черепашки (turtle).")
    tr.done()

if __name__ == "__main__":
    main()
