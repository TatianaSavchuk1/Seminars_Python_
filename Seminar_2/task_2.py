# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

import fractions


def func_sum (fract_1, fract_2):
    a, b = map(int, fract_1.split("/"))
    c, d = map(int, fract_2.split("/"))

    if b == d:
        if a + c == b:
            print(1)
        else:
            print (f'{a + c}/{b}')
    elif a*d + c*b == b*d:
        print(1)
    else:
        print (f'{a*d + c*b}/{b*d}')



def func_prod (fract_1, fract_2):
    a, b = map(int, fract_1.split("/"))
    c, d = map(int, fract_2.split("/"))
    
    print (f'{a * c}/{b * d}')

fract_1 = input('Введите первую дробь: ')
fract_2 = input('Введите вторую дробь: ')

func_sum (fract_1, fract_2)
func_prod (fract_1, fract_2)

# Проверка через fractions

x = fractions.Fraction(fract_1)
y = fractions.Fraction(fract_2)
sum1 = x + y
prod2 = x * y

print (sum1)
print (prod2)
