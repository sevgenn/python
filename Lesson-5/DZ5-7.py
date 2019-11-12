'''
Задание 7:
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
'''

import json

profit_list = []
profit = {}
average_profit = {}
sum_average = 0

with open('text_7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        temp = line.split()
        key = temp[0]
        value = int(temp[2]) - int(temp[3])
        profit[key] = value
        if value > 0:
            sum_average += value
average_profit['sum_average'] = sum_average / len(temp)
print(profit)
print(average_profit)
profit_list.append(profit)
profit_list.append(average_profit)
print(profit_list, end='\n\n')

with open('text_7.json', 'a') as wr_f:
    json.dump(profit_list, wr_f)
json_str = json.dumps(profit_list)
print(json_str)




