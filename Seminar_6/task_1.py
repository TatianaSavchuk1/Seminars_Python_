# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
# и возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# И весь период действует григорианский календарь. Проверку года на високосность вынести в отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys


def _is_leap_year(year):

    if year%4==0 and year%100!= 0 or year%400==0:
        return True
    else:
        return False


def check_date(date):

    d, m, y = (int(i) for i in date)
    long_months = [1, 3, 5, 7, 8, 10, 12]
    short_months = [4, 6, 9, 11]
    feb = 2

    if y > 0 and y < 10000 and m > 0 or m < 13:      
            if m in long_months and d > 0 and d < 32:
                return True
            elif m in short_months and d > 0 and d < 31:
                return True
            elif m == feb:
                if _is_leap_year(y) == True and d > 0 and d < 30:
                    return True
                elif _is_leap_year(y) == False and d > 0 and d < 29:
                    return True
            else:
                return False
    else:
        return False
    

date = input('Введите дату в формате DD.MM.YYYY: ').split('.')
# print(check_date(date))


if __name__ == '__main__':
    print(check_date(date))
    date = sys.argv
    print(sys.argv)
    











