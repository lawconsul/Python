# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

def create_dir(dir_name):
    full_path = os.path.join(os.getcwd(),dir_name)
    try:
        os.mkdir(full_path)
        print("Folder {} created".format(full_path))
    except FileExistsError:
        print("Folder {} exists".format(full_path))

def create_dir_range(start, end):
    for i in range(start,end+1):
        create_dir(str(i))

def delete_dir(dir_name):
    full_path = os.path.join(os.getcwd(),dir_name)
    try:
        os.removedirs(full_path)
        print("Folder {} deleted".format(full_path))
    except FileExistsError:
        print("Folder {} exists".format(full_path))

def delete_dir_range(start, end):
    for i in range(start,end+1):       
        delete_dir(str(i))


if __name__ == "__main__":
	create_dir("test_dir")
	create_dir_range(1, 9)
	delete_dir_range(1, 9)





# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_dir():
    full_path = os.path.join(os.getcwd())
    print("Folder {} contain:".format(full_path))
    try:
	    [print(dir) 
	     for root, dirs, files in os.walk(".")  
	        for dir in dirs]

    except FileNotFoundError:
    	print("Folder {} not found".format(full_path))


if __name__ == "__main__":
	show_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
import sys
def clone_py():
    full_path = str(sys.argv[0])
    print(full_path)
    shutil.copyfile(full_path, full_path + '.dupl')

if __name__ == "__main__":
	clone_py()
