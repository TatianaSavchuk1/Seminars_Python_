# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

money = 0
amount = 0
count_operations = 0


while money >= 0:
    option = int(input('Выберите опцию: 1. Положить, 2. Снять, 3. Выйти'))

    if money > 5000000:
        money -= money*10/100


    if option == 1:
        count_operations += 1
        if count_operations % 3 == 0:
            money += money*3/100
        amount = int(input('Введите сумму: '))
        if amount % 50 == 0:
            money += amount
        else:
            print('Введите сумму, кратную 50')
        print (f'На Вашем счету {money} рублей')
        
        
    
    elif option == 2:
        count_operations += 1
        if count_operations % 3 == 0:
            money += money*3/100
        amount = int(input('Введите сумму: '))
        if amount % 50 == 0:
            if amount*1.5/100 >= 30 and amount*1.5/100 <= 600:
                money -= amount + amount*1.5/100
            else:
                money -= amount
        else:
            print('Введите сумму, кратную 50')
        print (f'На Вашем счету {money} рублей')

        
    
    elif option == 3:
        print('До-свидания!')
        print (f'На Вашем счету {money} рублей')
        break

    
    else:
        print('Введите 1, 2 или 3')
        

        