# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math as m
list1 = [0, 26, -9, 4, -16, 1, 9]
list2 = [0]
for i in list1:
    if (i >= 0):
        s = m.sqrt(i)
        if int(s) - s == 0:
            list2.append(s)
for i in list2:
    print(i)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = "30.01.2013"
DATE = ''

day_list = ["Первое", "Второе", "Третье", "Четвертое", "Пятое", "Шестое", "Седьмое", "Восьмое", "Девятое", 
            "Десятое", "Одинадцатое", "Двенадцатое", "Тринадцатое", "Четырнадцатое", "Пятнадцатое",
            "Шестнадцатое", "Семнадцатое", "Восемнадцатое", "Девятнадцатое", "Двадцатое", "Двадцать первое", 
            "Двадцать второе", "Двадцать третье", "Двадцать четвертое", "Двадцать пятое", "Двадцать шестое",
            "Двадцать седьмое", "Двадцать восьмое", "Двадцать девятое", "Тридцатое", "Тридцать первое" ]
day = int(date[0:2])
month_list = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
month = int(date[3:5])
year = date[-4:]
DATE = " ".join([day_list[day-1], month_list[month-1], year, "года"])
print(DATE)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
n = int(input("Введите число: "))
list1=[]
i = 0
while i < n:
    list1.append(random.randint(-100,100))
    i = i + 1
print(list1)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка::
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list1 = [1,2,1,5,4,7,4,5,5,8]
list0 = []
set1 = set(list1)
set0 = set(list0)

# а) неповторяющиеся элементы исходного списка:
list_base = (set1 ^ set0)
print(list_base)
# б) элементы исходного списка, которые не имеют повторений
for i in list_base:
    list1.remove(i)
set_repeat = set(list1)
set_norepeat = set(list_base) - set_repeat
print(set_norepeat)
