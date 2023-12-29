from authorization import auth

balance = 0.0

def cash_in(summa):
    global balance
    balance += summa
    print("Ваш счёт пополнен на "f'{summa}', "\nБаланс: ", balance)

def cash_out(summa):
    global balance
    if summa > balance:
        print("Недостаточно средств!")
    else:
        balance -= summa
        print("Вы сняли "f'{summa}', "\nБаланс: ", balance)

while True:
    login = str(input("Hello! Please, log in!\n"))
    password = str(input("Please, type your password!\n"))
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
            summa = float(input("Введите сумму для снятия: "))
            cash_out(summa)
        elif choise == 2:
            summa = float(input("Положите деньги в банкомат "))
            cash_in(summa)
        elif choise == 3:
            break
    except ValueError:
        print('Некорректный ввод')
