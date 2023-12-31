import sqlite3
import re

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


#Функция проверки пароля на сложность
def password_check(password):
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