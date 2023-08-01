# Напишите программу, которая получает целое число 
# и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def hex_num (num, n = 16):
    result = ''
    hex_digits = "0123456789abcdef"
    while num != 0:
        result = hex_digits[num % n] + result
        num = num // n
    return result 

num = int(input('Enter a number: '))
print(hex_num(num))
print(hex(num))