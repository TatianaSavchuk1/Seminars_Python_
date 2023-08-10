# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt

# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')



def path_to_tuple (path):
    
    path = path.split('/')
    res = ()
        
    *a,b = (i for i in path)
    b, c = b.split('.')
    res = a, b, c
    return res


print(path_to_tuple('c:/Users/Vladislav/Desktop/deep_to_python/test.txt'))
