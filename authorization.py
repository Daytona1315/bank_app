import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()


def auth(login:str, password:str):
    current_user: str = 'none'
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


def register(login:str, password:str, first_name:str, last_name:str):
    sql.execute(f"SELECT * FROM users WHERE Login = '{login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users (Login, Password, FirstName, LastName) "
                    f"VALUES ('{login}', '{password}', '{first_name}', '{last_name}')")
        db.commit()
        print('Регистрация прошла успешно!')
        return True
        sql.close()
        db.close()
    else:
        print(f'Пользователь {login} уже существует. Выберите другой логин.')
        return False