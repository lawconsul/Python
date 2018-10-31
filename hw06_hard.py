# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import re
import os

class Worker:
    def __init__(self, name, surname, offer, post, hour_norm):
        self.name = name
        self.surname = surname
        self.offer = int(offer)
        self.post = post
        self.hour_norm = int(hour_norm)
        self.hour_work = 0
        self.pay = 0

    def get_full_name(self):
        return self.surname + ' '+ self.name

    def set_name(self, new_name):
        self.name = new_name

    def set_hour_work(self, hour_work):
        self.hour_work = int(hour_work)
    
    def check(self):     
        pay_per_hour = self.offer / self.hour_norm
        self.pay = self.offer
        diff = self.hour_work - self.hour_norm
        if diff > 0:
            self.pay = self.offer + diff * 2 * pay_per_hour
        else:
            self.pay = self.offer + diff * pay_per_hour

def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

def get_workers(esc_line, file_name, Workers):
    lineX = 0  
    f = open(os.path.join(os.getcwd(), file_name), 'r')
    for line in f.readlines():
        if lineX >= esc_line:
            print (line)
            pattern = r"\S+"
            r = re.findall(pattern,  line)

            if isinteger(r[0]) == False and isinteger(r[1]) == False and isinteger(r[2]) and isinteger(r[3]) == False and isinteger(r[4]):
                worker = Worker(r[0], r[1], r[2], r[3], r[4])
                Workers.append(worker)

        lineX += 1
    f.close()

def get_hours(esc_line, file_name, Workers):
    lineX = 0  
    f = open(os.path.join(os.getcwd(), file_name), 'r')
    for line in f.readlines():
        if lineX >= esc_line:
            print (line)
            pattern = r"\S+"
            r = re.findall(pattern,  line)

            if isinteger(r[0]) == False and isinteger(r[1]) == False and isinteger(r[2]):
                for worker in Workers:
                    if worker.name == r[0] and worker.surname == r[1]:
                        worker.set_hour_work(r[2])
                        worker.check()

        lineX += 1
    f.close()


Workers = []
get_workers(1, r"data/workers", Workers)
get_hours(1, r"data/hours_of", Workers)
pass