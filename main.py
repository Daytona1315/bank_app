from authorization import auth, register
from functions import *


# Стартовое окно
def main():
    while True:
        print("Зарегистрировать новый аккаунт - введите 1\n"
              "Войти в существующий аккаунт - введите 2\n"
              "Выйти из приложения - введите 3\n")
        message = input()
        if message == "1":
            user_reg()
        elif message == "2":
            user_auth()
        else:
            break


# Регистрация
def user_reg():
    while True:
        while True:
            login = input("Придумайте логин: \n")
            result = login_check(login)
            if result == False:
                print(f"Пользователь {login} уже существует!")
                continue
            else:
                break
        while True:
            password = input("Придумайте пароль: \n")
            result = password_check(password)
            if result == True:
                break
            else:
                print(result)
                continue
        while True:
            first_name = input("Введите имя: \n")
            last_name = input("Введите фамилию: \n")
            result = register(login, password, first_name, last_name)
            if result == False:
                print("Такой пользователь уже существует")
                continue
            else:
                print("Успешная регистрация! \n")
                menu(login, password, first_name, last_name)


# Вход в аккаунт
def user_auth():
    while True:
        login = str(input("Введите логин: \n"))
        password = str(input("Введите пароль: \n"))
        y = auth(login, password)
        if y == 1:
            print("Такого пользователя не существует")
        elif y == 2:
            print("Неверный пароль!")
        elif y == 3:
            names = get_name(login)
            first_name, last_name = names[0], names[1]
            menu(login, password, first_name, last_name)


# Главное меню
def menu(login, password, first_name, last_name):
    while True:
        print(f"Здравствуйте {first_name.title()} {last_name.title()}!\n"
              f"Что вы хотите сделать сегодня?\n"
            "Введите '1' чтобы снять деньги\n"
            "Введите '2' чтобы пополнить счёт\n"
            "Введите '3' чтобы узнать баланс счёта\n"
            "Введите '4' чтобы выйти\n")
        try:
            choise = int(input())
            if choise == 1:
                amount = float(input("Введите сумму для снятия: \n"))
                msg = withdraw(login, password, amount)
                if msg == 1:
                    print("Ошибка!Попробуйте ввести другие даннные\n")
                elif msg == 2:
                    print("Недостаточно средств!\n")
                elif msg == 3:
                    print("Успешно снято -", amount, "руб\n")
            elif choise == 2:
                amount = float(input("Положите деньги в банкомат: \n"))
                deposit(login, amount)
                print("Успешное пополнение -", amount, "руб\n")
            elif choise == 3:
                print("Баланс -", check_balance(login), "руб\n")
            elif choise == 4:
                exit()
        except ValueError:
            print('Некорректный ввод')


# Старт программы
main()
