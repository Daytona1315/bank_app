from authorization import auth, register
from functions import check_balance, deposit, withdraw

while True:
    try:
        choise = int(input('Войдите (1) или зарегистрируйтесь (2): '))
        if choise == 1:
            login = str(input("Введите логин\n"))
            password = str(input("Введите пароль\n"))
            if auth(login, password) == True:
                break
            else:
                continue
        else:
            break
    except ValueError:
        print('Введите 1 чтобы войти или 2 чтобы зарегистрироваться')

while True:
    login = input("Придумайте логин: \n")
    password = str(input("Придумайте пароль: \n"))
    first_name = input("Введите имя: \n")
    last_name = input("Введите фамилию: \n")
    register(login, password, first_name, last_name)
    break


while True:
    print("Что вы хотите сделать сегодня?\n"
          "Введите '1' чтобы снять деньги\n"
          "Введите '2' чтобы пополнить счёт\n"
          "Введите '3' чтобы узнать баланс счёта\n"
          "Введите '4' чтобы выйти\n")
    try:
        choise = int(input())
        if choise == 1:
            amount = float(input("Введите сумму для снятия: "))
            withdraw(login, password, amount)
        elif choise == 2:
            amount = float(input("Положите деньги в банкомат "))
            deposit(login, amount)
        elif choise == 3:
            print(check_balance(login))
        elif choise == 4:
            break
    except ValueError:
        print('Некорректный ввод')