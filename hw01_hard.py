
__author__ = 'Савельев А. С.'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Подсказка: это значение точно есть ;)

# Вначале a предположил что было введено: a = True, a == a**2 возвращает True,
# но a == a*2 возвращает False, a > 999999 - тоже False.
# Признаюсь, я погуглил и нашел решение:
# a = float('inf')
# Получается мы переменной a присавиваем значение математической бесконечности,
# а она (бесконечнось) уже удовлетворяет всем трем условиям