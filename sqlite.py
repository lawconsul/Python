# 
import os
import sqlite3
import datetime

class Sqlite():
    # Создание файла базы данных
    def __init__(self):
        self._db_filename = 'openweather.db'
        #conn = sqlite3.connect(db_filename)
        #conn.close()

    def db_filename(self):
        return self._db_filename

    def delete(self):
        os.remove(self._db_filename)


    # Создание схемы
    # Схема определяет таблицы в базе данных
    def create(self):
        with sqlite3.connect(self.db_filename()) as conn:
            conn.cursor()
            conn.execute("""
                CREATE TABLE IF NOT EXISTS meteo (
                id_city INTEGER PRIMARY KEY,
                name_city VARCHAR(255),
                date DATE,
                temp INTEGER,
                id_weather INTEGER
                );
                """)
            #conn.close()

    # Insert
    def insert(self, id_city, name_city, temp, id_weather):
        with sqlite3.connect(self.db_filename()) as conn:
            conn.execute("""
                insert into meteo (id_city, name_city, date, temp, id_weather) VALUES (?,?,?,?,?)""", (
                    '%s'%id_city, 
                    '%s'%name_city, 
                    datetime.date.today(),
                    '%s'%temp,
                    '%s'%id_weather
                )
            )
          #  conn.close()

    def print(self):
        with sqlite3.connect(self.db_filename()) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("select * from meteo")
            for row in cur.fetchall():
                #print(row)
                id_city, name_city, date, temp, id_weather = row
                print(id_city, name_city, date, temp, id_weather)
           # conn.close()

    def rows2export(self):
        with sqlite3.connect(self.db_filename()) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("select * from meteo")
        return cur.fetchall()


    def update(self, id_city, name_city, temp, id_weather):
        with sqlite3.connect(self.db_filename()) as conn:
            # Select
            # Объекты connection имеют атрибут row_factory, который позволяет вызывать
            # код, контролирующий тип объкта, создаваемого для каждой строки в запросе
            # Объекты Row дают доступ к данным по индексу и имени
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            # Update
            cur.execute("update meteo set date=:date, temp=:temp, id_weather=:id_weather where id_city=:id_city", 
                {'date': datetime.date.today(), 'id_city': id_city, 'temp':temp, 'id_weather':id_weather })

            conn.commit()
            cur.close()

    def contain(self, id_city):
        contain = False
        with sqlite3.connect(self.db_filename()) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("select id_city from meteo  where id_city=:id_city", 
                {'id_city': id_city })
            for row in cur.fetchall():
                contain = True
        return contain








