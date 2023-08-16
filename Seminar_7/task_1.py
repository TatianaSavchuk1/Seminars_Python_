# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

# Чтобы записать байты можно использовать список с числами и функцию bytes

from random import choice, randint
import numpy as np


VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'


def generate_name (min_name_len = 6, max_name_len = 30):
    rword = ''
    for _ in range(min_name_len, max_name_len + 1):
        rword += choice(VOWELS + CONSONANTS)
    return rword   

    
def generate_bytes (min_byte_num = 256, max_byte_num = 4096):   
    for byte in range(min_byte_num, max_byte_num + 1):
        rbytes = np.random.default_rng().bytes(byte)
    return rbytes
    
    
def generate_files (ext = 'w', files_amount = 42):    
    for _ in range(files_amount):
        with open (generate_name(6, 30), ext) as f:
            f.write(str(generate_bytes(256, 4096)))



if __name__ == '__main__':
    generate_files()

