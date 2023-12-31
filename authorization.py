import sqlite3


def auth(login:str, password:str):
    current_user: str = 'none'
    sql.execute(f"SELECT Login FROM users WHERE Login = '{login}'")
    if sql.fetchone() is None:
       return 1
       db.close()
       sql.close()
    else:
         sql.execute(f"SELECT Password FROM users WHERE Password = '{password}'")
         if sql.fetchone() is None:
            return 2
            db.close()
            sql.close()
         else:
            current_user = login
            return 3
            db.close()
            sql.close()



def register(login:str, password:str, first_name:str, last_name:str):
    sql.execute(f"SELECT * FROM users WHERE Login = '{login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users (Login, Password, FirstName, LastName) "
                    f"VALUES ('{login}', '{password}', '{first_name}', '{last_name}')")
        db.commit()
        return True
        db.close()
        sql.close()

    else:
        return False
        db.close()
        sql.close()