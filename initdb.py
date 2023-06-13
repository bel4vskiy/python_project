import sqlite3

con = sqlite3.connect('people.db')
cur = con.cursor()
# sql_query = '''INSERT INTO loginpsw(login, password) VALUES('pobeda', 'pobeda123')'''
# cur.execute(sql_query)
# con.commit()
# cur.close()

def check_access(cur, con, user, password):
        cur.execute(f'''SELECT login, password FROM loginpsw WHERE login="{user}"''')
        all_results = cur.fetchall()
        print(all_results)
        if all_results == []:
            return False



check_access(cur, con, 'pobeda', 'pobeda123')