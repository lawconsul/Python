# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import hw05_easy

def walk2dir(dir_name):
    full_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(full_path)
        print("Успешно перешел в подкаталог {}".format(dir_name))
    except FileNotFoundError:
        print("Folder {} not exists".format(full_path))

def select_tool():
    print("Что будем делать?")
    print("1. Перейти в папку")
    print("2. Просмотреть содержимое текущей папки")
    print("3. Удалить папку")
    print("4. Создать папку")
    print("5. Выйти")

    
    do = int(input())    
    while do in range(1,5):
        if do == 1:
            print("Укажите имя папки?")
            dir_name = str(input())
            walk2dir(dir_name)
            do = None
            select_tool()

        if do == 2:
            hw05_easy.show_dir()
            do = None
            select_tool()

        if do == 3:
            print("Укажите имя папки?")
            dir_name = str(input())
            hw05_easy.delete_dir(dir_name)
            do = None
            select_tool()

        if do == 4:
            print("Укажите имя папки?")
            dir_name = str(input())
            hw05_easy.create_dir(dir_name)
            do = None
            select_tool()


        if do == 5:
            return()

select_tool()

