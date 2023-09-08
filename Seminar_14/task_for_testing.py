import sys


def is_leap_year(year):

    """
    >>> is_leap_year(2023)
    False

    >>> is_leap_year(2024)
    True
    """

    if year%4==0 and year%100!= 0 or year%400==0:
        return True
    else:
        return False
    

def check_year(y):

    """
    >>> check_year(2023)
    True

    >>> check_year(0)
    False

    >>> check_year(10000)
    False
    """

    if y > 0 and y < 10000:
        return True
    else:
        return False
    

def check_month(m):

    """
    >>> check_month(0)
    False

    >>> check_month(12)
    True

    >>> check_month(13)
    False
    """

    if  m > 0 and m < 13:      
        return True
        
    else:
        return False
    

def check_day(d, m, y):

    """
    >>> check_day(32, 11, 2023)
    False

    >>> check_day(31, 10, 2023)
    True

    >>> check_day(29, 2, 2023)
    False

    >>> check_day(29, 2, 2024)
    True
    """

    if m in long_months and d > 0 and d < 32:
        return True
    elif m in short_months and d > 0 and d < 31:
        return True
    elif m == feb:
        if is_leap_year(y) == True and d > 0 and d < 30:
            return True
        if is_leap_year(y) == False and d > 0 and d < 29:
            return True
        else:
            return False

    else:
        return False




# def check_date(date):

#     d, m, y = (int(i) for i in date)
#     long_months = [1, 3, 5, 7, 8, 10, 12]
#     short_months = [4, 6, 9, 11]
#     feb = 2




#     if y > 0 and y < 10000 and m > 0 or m < 13:      
#             if m in long_months and d > 0 and d < 32:
#                 return True
#             elif m in short_months and d > 0 and d < 31:
#                 return True
#             elif m == feb:
#                 if is_leap_year(y) == True and d > 0 and d < 30:
#                     return True
#                 elif is_leap_year(y) == False and d > 0 and d < 29:
#                     return True
#             else:
#                 return False
#     else:
#         return False
    

date = input('Введите дату в формате DD.MM.YYYY: ').split('.')
d, m, y = (int(i) for i in date)
long_months = [1, 3, 5, 7, 8, 10, 12]
short_months = [4, 6, 9, 11]
feb = 2


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)

    # print(check_date(date))
    # date = sys.argv
    # print(sys.argv)