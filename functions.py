import sqlite3


def check_balance(login:str):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT Balance FROM users WHERE Login = '{login}'")
    balance = sql.fetchone()
    return balance[0]
    sql.close()
    db.close()


def deposit(login:str, amount:float):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE users SET Balance = Balance + {amount} WHERE Login = '{login}'")
    db.commit()
    return True
    sql.close()
    db.close()


def withdraw(login:str, password:str, amount:float):
    # Функция требует логин, пароль (как дополнительное подтверждение), и сумму денег для снятия

    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT Balance FROM users WHERE Login = '{login}' AND Password = '{password}'")

    # Если указанные данные не найдены, функция возвращает False
    if sql.fetchone() is None:
        return 1

    else:
        sql.execute(f"SELECT Balance FROM users WHERE Login = '{login}' AND Password = '{password}'")

        # Получаем текущий баланс и записываем его в переменную current_balance
        current_balance = sql.fetchone()

        # Если текущий баланс больше или равен сумме, то деньги списываются и функция возвращает True
        if current_balance[0] >= amount:
            sql.execute(f"UPDATE users SET Balance = Balance - {amount} "
                        f"WHERE Login = '{login}' AND Password = '{password}'")
            db.commit()
            return 3
            sql.close()
            db.close()

        # Если текущий баланс меньше чем запрашиваемое кол-во денег, функция возвращает False
        else:
                return 2