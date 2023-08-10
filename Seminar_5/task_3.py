#Создайте функцию генератор чисел Фибоначчи


def fibonacchi(N):
    a, b = 1, 1
    for _ in range(N):
        yield a
        a, b = b, a + b


print (list(fibonacchi(10)))