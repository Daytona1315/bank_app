import sqlite3
import re

# Проверка баланса
def balance_check(login:str):
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
    else:
        sql.execute(f"SELECT Balance FROM users WHERE Login = '{login}' AND Password = '{password}'")
        current_balance = sql.fetchone()
        if current_balance[0] >= amount:
            sql.execute(f"UPDATE users SET Balance = Balance - {amount} "
                        f"WHERE Login = '{login}' AND Password = '{password}'")
            db.commit()
            return 3
        else:
            return 2
    db.close()
    sql.close()

def send_money(login, recipient, amount):
    try:
        db = sqlite3.connect('server.db')
        sql = db.cursor()
        sql.execute(f"UPDATE users SET Balance = Balance - {amount} WHERE Login = '{login}'")
        db.commit()
        sql.execute(f"UPDATE users SET Balance = Balance + {amount} WHERE Login = '{recipient}'")
        db.commit()
        return True
    except Exception:
        return False
    db.close()
    sql.close()

# Функция проверки пароля на сложность
def password_difficulty(password):
    if len(password) < 8:
        return "Пароль слишком короткий. Длина пароля должна быть не менее 8 символов."
    if not re.search(r"[A-Z]", password):
        return "Пароль должен содержать хотя бы одну букву в верхнем регистре."
    if not re.search(r"[a-z]", password):
        return "Пароль должен содержать хотя бы одну букву в нижнем регистре."
    if not re.search(r"\d", password):
        return "Пароль должен содержать хотя бы одну цифру."
    if not re.search(r"\W", password):
        return "Пароль должен содержать хотя бы один специальный символ."
    return True


# Проверка логина по базе данных
def login_check(login):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT Login FROM users WHERE Login = '{login}'")
    if sql.fetchone() is None:
        return True
    else:
        return False
    db.close()
    sql.close()


def password_check(login, password):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT Password FROM users WHERE Login = '{login}'"
                f"AND Password = '{password}'")
    if sql.fetchone() is None:
        return False
    else:
        return True
    db.close()
    sql.close()


def get_name(login):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"SELECT FirstName, LastName FROM users WHERE Login = '{login}'")
    name, *names = (sql.fetchall())
    if name is None:
        return False
    else:
        return name
    db.close()
    sql.close()