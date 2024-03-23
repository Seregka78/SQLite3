from Procedure.proc import ADD_info, All_print_consol, ADD_basa, create_connection, ADD_colum, corect_info
import sqlite3

# con = sqlite3.connect('../sqlite3.db') #Создаем подключение к базе данных к файлу с наружи
# cur = con.cursor()
path = 'sqlite3.db'

connect = create_connection(path)
# Строка определяет функцию create_connection(),
# которая принимает путь к базе данных SQLite.

#ADD_colum(connect, 'DATA_MODE') # добовление колонки


print('для вывода всей информации - "ALL", для добавления в базу "ADD", для изменения информации в базе "CORE"')
# sms = ''
sms = str(input('Выберите вариант \n'))
print(sms)
if sms == "ADD":
    ADD_info(connect)
elif sms == "ALL":
    All_print_consol(connect)
elif sms == "CORE":
    corect_info(connect)
else:
    print("Ввели не верный запрос")





connect.commit()

connect.close()