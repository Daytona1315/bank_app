from authorization import auth, register
from functions import check_balance, deposit, withdraw

def menu(login, password):
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
                exit()
        except ValueError:
            print('Некорректный ввод')


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

def main():
    while True:
        print("1 - Регистрация\n"
              "2 - Авторизация\n"
              "3 - Выход")
        
        message = input()

        if message == "1":
            user_reg()
        elif message == "2":
            user_auth()
        else:
            break

main()