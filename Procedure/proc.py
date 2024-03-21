import sqlite3
con=sqlite3.connect('sqlite3.db') #Создаем файл с базой данных
cur = con.cursor()
def ADD_info():
    x = 0
    i = int(input('Введите сколько моделей хотите добавить в базу данных'))

    for x in range(i):
        md = str(input('Укажите производителя'))
        ml = str(input('Укажите модель'))
        n = str(input('Укажите серийный номер'))
        print(f'''добавили {x + 1}''')
        x += 1
        cur.execute(" INSERT INTO car (mode, model, name_id) VALUES(?,?,?);", (md, ml, n))
        #
        # В документации написано, что метод принимает два аргумента - строку запроса и кортеж аргументов
        # cur.execute("INSERT INTO names VALUES(?, ?, ?);", (name, age, gender))
        con.commit()

def All_print_consol():
    res = cur.execute('SELECT * FROM car')                  #вывести в консоль все
    print('Вот что сейчас в базе данных', res.fetchall())
