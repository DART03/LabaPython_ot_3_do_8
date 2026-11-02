#Лабораторная работа номер 4 вариант 3

from random import randint

n = int(input("Введите количество элементов в массиве N (<= 30): "))
if n > 30: n = 30
elif n < 5: n = 5

# Генерация целочисленного массива от -5 до 5
mas = [randint(-5, 5) for _ in range(n)]
print("Начальный массив:", mas)

#Произведение элементов с четными номерами (индексы 0, 2, 4...)
prod = 1
for i in range(0, len(mas), 2):
    prod *= mas[i]

#Сумма элементов между первым и последним нулевыми элементами
first_zero = -1
last_zero = -1
for i in range(len(mas)):
    if mas[i] == 0:
        if first_zero == -1:
            first_zero = i
        last_zero = i

sum_between = 0
if first_zero != -1 and last_zero != -1 and last_zero - first_zero > 1:
    sum_between = sum(mas[first_zero + 1 : last_zero])

#Преобразование массива
positives = [x for x in mas if x >= 0]
negatives = [x for x in mas if x < 0]
transformed_mas = positives + negatives

# Вывод результатов
print(f"1. Произведение элементов с четными номерами: {prod}")
print(f"2. Сумма между первым и последним нулями: {sum_between}")
print(f"3. Преобразованный массив: {transformed_mas}")
