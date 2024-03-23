import sqlite3
from sqlite3 import Error
# Строки – импорт sqlite3 и класса Error.


def create_connection(path):
    connect = None
    try:
        connect = sqlite3.connect(path) #Создаем файл с базой данных
        print("Connection to SQLite DB successful")   #выводится состояние успешного подключения к базе данных.
    except Error as e:
        print(f"The error '{e}' occurred")
    return connect
#перехватывает любое  исключение, которое может быть
# получено, если методу.connect() не удастся установить соединение
# В следующей строке-сообщение об ошибке

def ADD_basa(connect):
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS car (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mode STRING,
            model STRING,
            name_id STRING) ''')
    cursor.close()

def ADD_info(connect):
    cursor = connect.cursor()
    x = 0
    i = int(input('Введите сколько моделей хотите добавить в базу данных \n'))

    for x in range(i):
        md = str(input('Укажите производителя\n'))
        ml = str(input('Укажите модель\n'))
        n = str(input('Укажите серийный номер\n'))
        cursor.execute(" INSERT INTO car (mode, model, name_id) VALUES(?,?,?);", (md, ml, n))
        print(f'''добавили {x + 1}''')
        x += 1
        #
        # В документации написано, что метод принимает два аргумента - строку запроса и кортеж аргументов
        # cur.execute("INSERT INTO names VALUES(?, ?, ?);", (name, age, gender))
    cursor.close()

def All_print_consol(connect):
    cursor = connect.cursor()
    res = cursor.execute('SELECT * FROM car')                  #вывести в консоль все
    print('Вот что сейчас в базе данных', res.fetchall())
    cursor.close()

def ADD_colum(connect, name_colum):
    cursor = connect.cursor()
    cursor.execute(f'''ALTER TABLE car ADD COLUMN {name_colum}''')
    print('добавили колонку\n', name_colum)
    cursor.close()


def corect_info(connect):
    cursor = connect.cursor()
    while True:
        All_print_consol(connect)
        id_info = int(input('Укажите ID строчки для  просмотра\n'))
        prnt_name=cursor.execute('PRAGMA table_info(car)')  #Вывод имени столбцов
        desc = prnt_name.fetchall()
        names = [fields[1] for fields in desc]              #выбираем первые элементы из списка
        print(names)
        resultat=cursor.execute(f''' SELECT * FROM car where id={id_info}''').fetchall()
        print('Выводим выбранную строку\n', resultat)
        SMS=str(input('Выберите имя столбца  для корректировки или EXT-для сохранения изменений и выхода\n'))

        if SMS=='EXT':
            break
        else:
            SMS_info = str(input('На какое значение поменять\n'))
            SMS_X=0
            for i in names:
                if SMS == i:
                    print('вы выбрали имя столбца для коректировки\n', i, '\n', 'хотите поменять на следующее значение ', SMS_info)
                    print(id_info)
                    cursor.execute(f'''UPDATE car SET {i} = ? WHERE id=?''', (SMS_info, id_info))
                    print('Выводим результат после изменений\n', resultat)
                    SMS_X+=1
            if SMS_X==0: print('Повторите попытку\n')
            #cursor.execute('UPDATE Users SET age = ?       WHERE username = ?',    (29, 'newuser'))
            #cursor.execute('UPDATE users SET user_status=? WHERE id=?',            ('normal',id))
        #INSERT INTO users (name, age) VALUES ('Tom', 22);
        #обновление инфо в строке: UPDATE work SET person = "tae" WHERE person = "tay";
        #UPDATE имя_таблицы SET имя_столбца = новое_значение WHERE условие
        #"""Update sqlitedb_developers set salary = 10000 where id = 4"""

    cursor.close()
