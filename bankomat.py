from authorization import auth
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
    login = str(input("Введите логин: "))
    password = str(input("Введите пароль: "))
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
