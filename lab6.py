#Лабораторная работа 6 вариант 3 

import numpy as np

def CountZeroColumns(Matr):
    nRow, nCol = Matr.shape
    count = 0
    for col in range(nCol):
        if 0 in Matr[:, col]:
            count += 1
    return count

def FindLongestSeriesRow(Matr):
    nRow, nCol = Matr.shape
    max_len, best_row = 0, 0
    for row in range(nRow):
        cur_len, row_max = 1, 1
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
    return best_row + 1

# Чтение из файла и запись результатов в файл
if __name__ == "__main__":
    input_file = "lab6_in.txt"
    output_file = "lab6_ou.txt"
    
    # 1. Чтение матрицы из файла
    with open(input_file, "rt", encoding="cp1251") as fi:
        MyMatr = np.loadtxt(fi, dtype=int, ndmin=2)
        
    # 2. Вычисления
    zero_cols = CountZeroColumns(MyMatr)
    target_row = FindLongestSeriesRow(MyMatr)
    
    # 3. Запись результатов в файл
    with open(output_file, "wt", encoding="cp1251") as fo:
        fo.write(" ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ №6 (ВАРИАНТ 3) \n")
        fo.write("Исходная матрица:\n")
        np.savetxt(fo, MyMatr, fmt="%5d")
        fo.write(f"\nРезультаты вычислений:\n")
        fo.write(f"1. Количество столбцов с нулями: {zero_cols}\n")
        fo.write(f"2. Номер строки с самой длинной серией: {target_row}\n")
        
    print(f"Обработка завершена. Данные успешно записаны в файл '{output_file}'.")
