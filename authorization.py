import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

current_user:str = 'none'



def auth(login:str, password:str):
    sql.execute(f"SELECT Login FROM users WHERE Login = '{login}'")
    if sql.fetchone() is None:
       print("Такого пользователя не существует!")
       return False
    else:
         sql.execute(f"SELECT Password FROM users WHERE Password = '{password}'")
         if sql.fetchone() is None:
            print('Неверный пароль!')
            return False
         else:
            current_user = login
            print('Авторизация прошла успешно!\nДобро пожаловать, 'f'{current_user.title()}')
            return True
            sql.close()
            db.close()




