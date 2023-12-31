from authorization import auth, register
from functions import *


# Стартовое окно
def main():
    while True:
        print("Зарегистрироваться - введите 1\n"
              "Войти в существующий аккаунт - введите 2\n"
              "Выйти из приложения - введите 3")
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
        login = input("Придумайте логин: \n")
        password = input("Придумайте пароль: \n")
        first_name = input("Введите имя: \n")
        last_name = input("Введите фамилию: \n")
        x = register(login, password, first_name, last_name)
        if x == False:
            print("Такой пользователь уже существует")
        else:
            print("Успешная регистрация")
            menu(login, password)


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
            menu(login, password)


# Главное меню
def menu(login, password):
    while True:
        print(f"{login.title()}, Что вы хотите сделать сегодня?\n"
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