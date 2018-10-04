# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruit = ["яблоко", "банан", "киви", "арбуз"]
for i,I in enumerate(fruit):
    print('{} {:>6}'.format(i+1,I))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

set1 = set([0, 2, 4, 6])
set2 = set([10, 8, 6, 4])
set1 - set2

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

list1 = [0, 2, 4, 6, 5, 3, 1]
list2 = []
for i in list1:
     list2.append(i*2) if i%2 else list2.append(i/4)
for i in list2:
    print(i)