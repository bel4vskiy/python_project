import sqlite3

class DB:
    global con, cur
    con = sqlite3.connect('people.db', check_same_thread=False)
    cur = con.cursor()



    def check_access(self, user, password):
        cur.execute(f'''SELECT id, login, password FROM loginpsw WHERE login="{user}"''')
        all_results = cur.fetchall()
        print(all_results)
        if all_results == []:
            return False
        elif all_results[0][2] == password:
            return True


    def add_user(self, user, password):
        sql_query = '''INSERT INTO loginpsw(login, password)
                        VALUES(?, ?);
                '''
        cur.execute(sql_query, (user, password))
        con.commit()
        return True