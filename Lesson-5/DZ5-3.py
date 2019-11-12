'''
Задание 3:
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

with open(r"F:\Test\text_3.txt", 'r') as f:
    content = f.readlines()
full_list = [pers.split() for pers in content]
min_list = [full_list[i][0] for i in range(len(full_list)) if int(full_list[i][1]) < 20000]
print(min_list)

# или так:
for el in min_list:
    print(el)

# или так:
for el in full_list:
    if int(el[1]) < 20000:
        print(el[0])

sum = 0
for i in range(len(full_list)):
    sum += int(full_list[i][1])
average_salary = sum / len(full_list)
print(f'Average salary is {average_salary}.')