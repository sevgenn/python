'''
Задание 2:
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке.
'''

try:
    with open('text_2.txt', 'r') as f:
        content = f.readlines()
        print(f'Quantity of strings is {len(content)}')
        if content:
            print('Quantity of words in each string:')
            i =1
            for elem in content:
                el_str = elem.split()
                print(f'{i} string --> {len(el_str)} words')
                i += 1
except IOError:
    print('Input-Output Error.')