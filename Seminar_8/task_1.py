# Напишите функцию, которая сереализует содержимое текущей директории в json-файл. 
# В файле должен храниться список словарей, словарь описывает элемент внутри директории: 
# имя, расширение, тип. Если элемент - директория, то только тип и имя. 
# Пример результата для папки, где лежит файл test.txt и директория directory_test:
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]

import os
import json


def directory_to_json(directory, content, res_list):
    direct_dict = {}
    file_dict = {}
    for element in directory:
        direct_dict = {'name': element, 'type': 'directory'}
        res_list.append(direct_dict)

    for element in content:
        file_dict = {'name': str(element.split('.')[:-1]), 'extention' : '.' + element.split('.')[-1], 'type' : 'file'}
        res_list.append(file_dict)
    
    return res_list
        

dir1 = str(os.path.abspath(__file__))
dir = dir1.split('\\')[:-1]

cont = os.listdir('d:\ТАНИНЫ ДЗ\PYTHON_ПОГРУЖЕНИЕ\Seminars\Seminar_8')
res = []


with open ('directory_or_file.json', 'w') as df:
    json.dump(directory_to_json(dir, cont, res), df, indent=4)




