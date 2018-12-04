__author__ = 'Савельев А. С.'

import random

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fib(n):
	if (n == 1 or n == 2):
		return 1
	return fib(n - 1) + fib(n - 2)

def fibonacci(n, m):
	a = []
	while n < m:
		a.append(fib(n))
		n += 1
	return a

print("\n\n\n\nЗадание-1:")
n = int(input("Введите начальный элемент ряда Фибоначчи: "))
m = int(input("Введите конечный элемент ряда Фибоначчи: "))
print("Ряд Фибоначчи с {}-элемента по {}-элемент:".format(n, m))
print(fibonacci(n, m))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
	n = 1
	while n < len(origin_list):
		for i in range(len(origin_list) - n):
			if origin_list[i] > origin_list[i + 1]:
				origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
		n += 1

a = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print("\n\nЗадание-2:")
print("\nДан список:")
print (a)
print("\nСортируем пузырьком:")
sort_to_max(a)
print (a)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(f, a):
	b = []
	for i in range(len(a)):
		if f(a[i]):
			b.append(a[i])
	return b

def func(x):
	if x > 0:
		return True
	else:
		return False

a = []
for i in range(20):
	a.append(random.randint(-100, 100))
print(a)

b = list(filter(func, a))
print(b)

c = list(my_filter(func, a))
print(c)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

