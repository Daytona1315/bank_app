import sqlite3


# Проверка баланса
def check_balance(login:str):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT Balance FROM users WHERE Login = '{login}'")
    balance = sql.fetchone()
    return balance[0]
    db.close()
    sql.close()


# Депозит денег на счёт
def deposit(login:str, amount:float):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE users SET Balance = Balance + {amount} WHERE Login = '{login}'")
    db.commit()
    return True
    db.close()
    sql.close()


# Снятие денег со счёта
def withdraw(login:str, password:str, amount:float):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT Balance FROM users WHERE Login = '{login}' AND Password = '{password}'")
    if sql.fetchone() is None:
        return 1
        db.close()
        sql.close()
    else:
        sql.execute(f"SELECT Balance FROM users WHERE Login = '{login}' AND Password = '{password}'")
        current_balance = sql.fetchone()
        if current_balance[0] >= amount:
            sql.execute(f"UPDATE users SET Balance = Balance - {amount} "
                        f"WHERE Login = '{login}' AND Password = '{password}'")
            db.commit()
            return 3
            db.close()
            sql.close()
        else:
            return 2
            db.close()
            sql.close()