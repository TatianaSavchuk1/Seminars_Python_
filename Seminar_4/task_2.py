# Напишите функцию принимающую на вход только ключевые параметры(kwargs) и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}

def reverse_kwargs (**kwargs):

    reverse_dict = dict(zip(kwargs.values(), kwargs.keys()))

    return reverse_dict


print(reverse_kwargs(rev=True, acc="YES", stroka=4))