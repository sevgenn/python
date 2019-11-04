'''
Задание 2:
Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def data_user(name, surname, dob, city, email, phone):
    data_base = dict()
    name = name.capitalize()
    surname = surname.capitalize()
    city = city.capitalize()
    phone = f'+7 ({phone[:3]}) {phone[3:6]}-{phone[6:8]}-{phone[8:]}'
    print(f'{surname + " " + name + "-":<25} dob: {dob:<10} city: {city:<15} email: {email:<15} phone: {phone:<15}')
    data_base[(surname, name)] = [dob, city, email, phone]
    return data_base

data_base = dict()
user_answer = 'Answer of an user'
while user_answer != 'Q':
    name = input('Enter a name - ')
    surname = input('Enter a surname - ')
    date_of_birthday = input('Enter a date of birthday - ')
    city_of_residence = input('Enter a city of residence - ')
    email = input('Enter user\'s email - ')
    phone_number = input('Enter user\'s phone number - ')

    data_base.update(data_user(name=name, surname=surname, dob=date_of_birthday, city=city_of_residence, email=email, phone=phone_number))
    user_answer = input('Enter any key to continue or "Q" to exit - ').upper()
print(data_base)
