# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.



# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name>")
    print("rm <file_name>")
    print("cd <full_path or relative_path>")
    print("ls")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def copy():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copyfile(file_path, file_path + '.dupl')
        print('создан дубликат файла {}: {}'.format(file_path, file_path + '.dupl'))
    except FileExistsError:
        print('дубликат файла {} уже существует'.format(file_path))


def rm():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), file_name)
    try:
        os.remove(file_path)
        print('из каталога {} удален файл {}'.format(os.getcwd(), file_name))
    except FileNotFoundError:
        print('файла с таким именем {} не существует'.format(file_name))



def cd():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if dir_name.startswith('/') and os.getcwd().startswith('/'):
    	full_path = dir_name
    elif dir_name.startswith(':',1) and os.getcwd().startswith(':',1):
    	full_path = dir_name
    else:
    	full_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(full_path)
        print("Успешно перешел в подкаталог {}".format(dir_name))
        print(os.getcwd())
    except FileNotFoundError:
        print("Директории {} не существует".format(full_path))

def ls():
	full_path = os.path.join(os.getcwd())
	print("Folder {} contain:".format(full_path))
	try:
	    [print(dir) 
	     for root, dirs, files in os.walk(".")  
	        for dir in dirs]
	    [print(file) 
	     for root, dirs, files in os.walk(".")  
	        for file in files]
	except FileNotFoundError:
		print("Folder {} not found".format(full_path))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy,
    "rm": rm,
    "cd": cd,
    "ls": ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")