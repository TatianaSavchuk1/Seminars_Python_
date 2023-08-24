# Создать декоратор для использования кэша. Т.е. сохранять аргументы и результаты в словарь, 
# если вызывается функция с агрументами, 
# которые уже записаны в кэше - вернуть результат из кэша, 
# если нет - выполнить функцию. Кэш лучше хранить в json.

import json


def json_logging (func: callable):
    try:
        with open (f'{func.__name__}.json', 'r') as data:
            result_list = json.load(data)
    except FileNotFoundError:
        result_list = []

    def wrapper (*args, **kwargs):

        result = func(*args, **kwargs)
        result_str = ''
        
        for arg in args:
            result_str += (str(arg))

        
        for dict in result_list:     
            for key in dict.keys():
                if str(key) == result_str:
                    print(dict)
                else:
                    result = func(*args, **kwargs)

        result_list.append({result_str : result})
              
        with open (f'{func.__name__}.json', 'w') as data:
            json.dump(result_list, data, indent=4)

        return result
    return wrapper


    
@json_logging
def count_sum (*args, **kwargs):
    return sum(args)




if __name__ == "__main__":
    sum_logging = json_logging(count_sum(5, 6, 7, 8))
    # sum_logging = json_logging(count_sum(1, 2, 3, 4))
    # sum_logging = json_logging(count_sum(7, 8, 9, 5))
    