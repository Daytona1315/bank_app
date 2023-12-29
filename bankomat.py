from authorization import *
balance = 0.0


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

    if login == "q":
        break
    else:
        register(login, password, first_name, last_name)

while True:
    login = str(input("Здравствуйте,войдите в систему\n"))
    password = str(input("Введите свой пароль\n"))
    if auth(login, password) == True:
        break
    else:
        continue


while True:
    print("Что вы хотите сделать сегодня?\n"
          "Введите '1' чтобы снять деньги\n"
          "Введите '2' чтобы пополнить счёт\n"
          "Введите '3' чтобы выйти")
    try:
        choise = int(input())
        if choise == 1:
            amount = float(input("Введите сумму для снятия: "))
            cash_out(amount)
        elif choise == 2:
            amount = float(input("Положите деньги в банкомат "))
            cash_in(amount)
        elif choise == 3:
            break
    except ValueError:
        print('Некорректный ввод')

