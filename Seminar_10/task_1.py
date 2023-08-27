# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), 
# которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства. 
# Задания должны решаться через вызов методов экземпляра.



class atm:

    def __init__(self, money: float, amount: float, count_operations: int):
        self.money = money
        self.amount = amount
        self.count_operations = count_operations


    
    def put_money(self):   
        self.count_operations += 1
        if self.count_operations % 3 == 0:
            self.money += self.money*3/100
        self.amount = int(input('Введите сумму: '))
        if self.amount % 50 == 0:
            self.money += self.amount
        else:
            print('Введите сумму, кратную 50')
        return f'На Вашем счету {self.money} рублей'


    def withdraw_money (self):    
        self.count_operations += 1
        if self.count_operations % 3 == 0:
            self.money += self.money*3/100
        self.amount = int(input('Введите сумму: '))
        if self.amount % 50 == 0:
            if self.amount*1.5/100 >= 30 and self.amount*1.5/100 <= 600:
                self.money -= self.amount + self.amount*1.5/100
            else:
                self.money -= self.amount
        else:
            print('Введите сумму, кратную 50')
        return f'На Вашем счету {self.money} рублей'


    def exit_atm (self):
        print('До-свидания!')
        return f'На Вашем счету {self.money} рублей'
        


operation = atm(0, 0, 0)
try_atm = 0

while try_atm == 0 :
    option = int(input('Выберите опцию: 1. Положить, 2. Снять, 3. Выйти'))

    if option == 1:
        print(operation.put_money()) 
    elif option == 2:
        print(operation.withdraw_money())
    elif option ==3:
        print(operation.exit_atm())
        break
    else:
        print('Введена несуществующая опция')



        

        