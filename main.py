#Лабораторная работа 5 вариант 3 

import numpy as np

def MakeIntegerMatr(n, m, a=-5, b=5):
    #Инициализация матрицы случайными целыми числами
    return np.random.randint(a, b + 1, size=(n, m))

def CountZeroColumns(Matr):
    #1. Подсчет столбцов, содержащих хотя бы один ноль
    nRow, nCol = Matr.shape
    count = 0
    for col in range(nCol):
        if 0 in Matr[:, col]:
            count += 1
    return count

def FindLongestSeriesRow(Matr):
    #2. Определение номера строки с самой длинной серией одинаковых элементов
    nRow, nCol = Matr.shape
    max_len = 0
    best_row = 0
    for row in range(nRow):
        cur_len = 1
        row_max = 1
        for col in range(1, nCol):
            if Matr[row, col] == Matr[row, col - 1]:
                cur_len += 1
            else:
                cur_len = 1
            if cur_len > row_max:
                row_max = cur_len
        if row_max > max_len:
            max_len = row_max
            best_row = row
    return best_row + 1  # Возвращаем номер строки с 1

# Основная программа
if __name__ == "__main__":
    n = int(input("Введите число строк N: "))
    m = int(input("Введите число столбцов M: "))
    
    MyMatr = MakeIntegerMatr(n, m, -3, 3)
    print("\nИсходная матрица:")
    print(MyMatr)
    
    zero_cols = CountZeroColumns(MyMatr)
    target_row = FindLongestSeriesRow(MyMatr)
    
    print("\nРезультаты (Лаб. №5, Вариант 3):")
    print(f"1. Количество столбцов с нулями: {zero_cols}")
    print(f"2. Номер строки с самой длинной серией: {target_row}")
