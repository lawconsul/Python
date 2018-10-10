# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    num = str(number)
    num1 = str(num[:num.index('.') + 1])
    num2 = str(num[num.index('.') + 1:num.index('.') + ndigits + 1])
    num3 = str(num[num.index('.') + ndigits + 1:num.index('.') + ndigits + 2])
   
    number = float(num1+num2)
    if float(num3) > 5:
        number += 10**(-ndigits)
    print(number)      
    
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

from functools import reduce
def lucky_ticket(ticket_number):
    n = str(ticket_number)
    while len(n) < 6:
        n = "0" + n
    
    n1 = n[:3]
    n2 = n[3:]
    
    N1 = list(map(int, n1))
    N2 = list(map(int, n2))
    
    sum1 = reduce(lambda a,x: a+x, N1)
    sum2 = reduce(lambda a,x: a+x, N2)
    
    return(sum1==sum2)


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
