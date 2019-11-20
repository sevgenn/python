'''
Задание 1:
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''

class Date:
    @classmethod
    def digit_class(cls, date):
        day, month, year = list(map(int, date.split('-')))
        print(f'{day:02d}.{month:02d}.{year:4d}')

    @staticmethod
    def digit_stat(date):
        day, month, year = date.split('-')
        dat = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30,
               '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}
        try:
            if day.isdigit() and month.isdigit() and year.isdigit() and 1 <= int(day) <= dat[month]:
                print(f'{int(day):02d}.{int(month):02d}.{int(year):4d}')
        except ValueError:
            print('It\'s not a digit.')
        finally:
            print('The program ended.')



inp = input('Enter date formated as "dd-mm-yyyy" - ')
Date.digit_class(inp)
today = Date()
today.digit_class(inp)

inp = input('Enter date formated as "dd-mm-yyyy" - ')
Date.digit_stat(inp)
tomorrow = Date()
tomorrow.digit_stat(inp)


