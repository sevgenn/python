'''
Задание 3:
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

'''Для простоты не учитываются ошибки ввода.'''

number = [[12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {'зима': (12, 1, 2), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}

# 1 вариант для списка:
month = int(input('Введите номер месяца для списка 1 вариант: '))
for i in range(len(number)):
    if month in number[i]:
        print(season_list[i])

# 2 вариант для списка:
month = int(input('Введите номер месяца для списка 2 вариант: '))
if 1 <= month <= 2 or month == 12:
    print(season_list[0])
elif 3 <= month <= 5:
    print(season_list[1])
elif 6 <= month <= 8:
    print(season_list[2])
elif 9 <= month <= 11:
    print(season_list[3])

# вариант для словаря:
month = int(input('Введите номер месяца для словаря: '))
for key in season_dict:
    if month in season_dict[key]:
        print(key)