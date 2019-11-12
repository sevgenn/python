'''
Задание 6:
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:    Информатика:   100(л)   50(пр)   20(лаб)
                        Физика:   30(л)   ​—​   10(лаб)
                        Физкультура:   ​—   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

with open('text_6.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

############### 1 Вариант ##########################

full_list = [subj.split() for subj in content]
print(full_list)
subj_dict = {}

for i in range(len(full_list)):
    if not full_list[i][0].isalpha():                      # Удаление двоеточия из наименования
        full_list[i][0] = full_list[i][0].rstrip(':')

    s = 0
    for j in range(1, len(full_list[i])):
        word = list(full_list[i][j])

        for letter in word[:]:
            if not letter.isdigit():                        # Удаление символов из числа
                word.remove(letter)
        full_list[i][j] = ''.join(word)

        if full_list[i][j].isdigit():
            s += int(full_list[i][j])

    subj_dict[full_list[i][0]] = s
print(subj_dict)
print()

############### 2 Вариант ##########################

subj_dict2 = {}
ord_dict = {ord(c): None for c in ':<>@#$%^&()/\.*-'}
print(content)
clear_line = [(content[i]).translate(ord_dict) for i in range(len(content))]

for i in range(len(clear_line)):
    clear_line[i] = clear_line[i].split()

    for j in range(1, len(clear_line[i])):
        clear_line[i][j] = ''.join(filter(lambda x: x.isdigit(), clear_line[i][j]))
    s2 = sum((int(n) for n in clear_line[i] if n.isdigit()))

    subj_dict2[clear_line[i][0]] = s2
print(subj_dict2)

