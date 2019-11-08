'''
Задание 1:
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в
час) + премия. Для выполнения расчета для конкретных значений необходимо запускать
скрипт с параметрами.
'''

######################### Вариант 1 №№№№№№№№№№№№##№№№№№№№№№№№№№№№№

from sys import argv

script_name, arg_1, arg_2, arg_3 = argv

def script_salary(rate, working_hours, bonus):
    salary = float(rate) * float(working_hours) + float(bonus)
    return salary

print(f'Salary is {script_salary(arg_1, arg_2, arg_3)}')


######################### Вариант 2 №№№№№№№№№№№№##№№№№№№№№№№№№№№№№

from sys import argv

script_name, arg_1, arg_2, arg_3 = argv

def script_salary(rate, working_hours, bonus):
    salary = float(rate) * float(working_hours) + float(bonus)
    print(f'Salary is {salary}')

script_salary(arg_1, arg_2, arg_3)
