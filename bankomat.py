from authorization import auth, register
from functions import check_balance

def cash_in(amount):
    global balance
    balance += amount
    print("Ваш счёт пополнен на "f'{amount}', "\nБаланс: ", balance)

def cash_out(amount):
    global balance
    if amount > balance:
        print("Недостаточно средств!")
    else:
        balance -= amount
        print("Вы сняли "f'{amount}', "\nБаланс: ", balance)

while True:
    login = input("Придумайте уникальный логин: \n")
    password = str(input("Придумайте пароль: \n"))
    first_name = input("Введите имя: \n")
    last_name = input("Введите фамилию: \n")

    register(login, password, first_name, last_name)
    break

while True:
    login = str(input("Введите логин\n"))
    password = str(input("Введите пароль\n"))
    if auth(login, password) == True:
        break
    else:
        continue

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
            cash_out(amount)
        elif choise == 2:
            amount = float(input("Положите деньги в банкомат "))
            cash_in(amount)
        elif choise == 3:
            print(check_balance(login))
        elif choise == 4:
            break
    except ValueError:
        print('Некорректный ввод')