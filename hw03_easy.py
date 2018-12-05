__author__ = 'Савельев А. С.'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


print("\n\n\n\nЗадание-1:")

def my_round(number, ndigits):
	exp = float(10 ** int(ndigits))
	tmp = int(float(number) * exp + 0.5)
	return tmp / exp

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
	if ticket_number < 100000:
		return False
	else:
		left = 0
		for i in range(3):
			left += ticket_number % 10
			ticket_number = int(ticket_number / 10)
		
		right = 0
		for i in range(3):
			right += ticket_number % 10
			ticket_number = int(ticket_number / 10)
		
		return left == right


print("\n\nЗадание-2:")
ticket = ''
while ticket != 'q':
	ticket = input("Введит номер билета (6 чисел): ")
	try:
		number = int(ticket)
	except ValueError:
		print("Вводите цифры 0-9 !\n")
	else:
		if (lucky_ticket(int(number))):
			print("Билет с номером {} является счастливым.\n".format(number))
		else:
			print("Билет с номером {} не является счастливым.\n".format(number))
