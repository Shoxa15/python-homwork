# ====== ЗАДАЧА 1 ======
# Дана сторона квадрата. Найти его периметр и площадь.

side = float(input("Введите сторону квадрата: "))
perimeter = 4 * side
area = side ** 2

print("Периметр квадрата:", perimeter)
print("Площадь квадрата:", area)


# ====== ЗАДАЧА 2 ======
# Дана длина диаметра. Найти длину окружности.

import math

diameter = float(input("Введите диаметр окружности: "))
length = math.pi * diameter

print("Длина окружности:", length)


# ====== ЗАДАЧА 3 ======
# Даны два числа a и b. Найти их среднее арифметическое.

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

mean = (a + b) / 2

print("Среднее арифметическое:", mean)


# ====== ЗАДАЧА 4 ======
# Даны два числа a и b. Найти сумму, произведение и квадраты.

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))

_sum = a + b
product = a * b
square_a = a ** 2
square_b = b ** 2

print("Сумма:", _sum)
print("Произведение:", product)
print("Квадрат a:", square_a)
print("Квадрат b:", square_b)
