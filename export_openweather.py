
""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sys
from openweather import city
from sqlite import Sqlite 
import pandas as pd

print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("export_openweather.py --csv file_name city_name")
    print("export_openweather.py --json file_name city_name")
    print("export_openweather.py --html file_name city_name")

def argv_check():
    error = False
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        error = True
    if not city_name:
        print("Необходимо указать название города третьим параметром")
        error = True
    return error

def export_csv():
    if argv_check():
        return

    # encoding = 'windows-1251'
    encoding = 'utf-8'
    with open(file_name, 'w', encoding=encoding) as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow( ('id_city', 'name_city', 'date', 'temp', 'id_weather') )
        
        SQL_wfc = Sqlite()
        rows = SQL_wfc.rows2export()
        for row in rows:
            id_city, name_city, date, temp, id_weather = row
            writer.writerow((id_city, name_city, date, temp, id_weather))

def export_json():
    if argv_check():
        return
    wfc_list = []
    SQL_wfc = Sqlite()
    rows = SQL_wfc.rows2export()
    
    for row in rows:
        id_city, name_city, date, temp, id_weather = row
        wfc = city('', id_city, name_city)  
        wfc.date = date
        wfc.temp = temp
        wfc.id_weather = id_weather
        wfc_json = json.dumps(wfc.__dict__)
        wfc_list.append(wfc_json)
    with open(file_name, 'w') as outfile:
        json.dump(wfc_list, outfile)
        

def id_weather2png(id_weather):
    return {
        200 <= id_weather < 232: '11d',
        300 <= id_weather < 321: '09d',
        500 <= id_weather < 504: '10d',   
              id_weather == 511: '13d',  
        521 <= id_weather < 531: '09d', 
        600 <= id_weather < 622: '13d',
        700 <= id_weather < 781: '50d',
              id_weather == 800: '01d',  
              id_weather == 801: '02d', 
              id_weather == 802: '03d', 
              id_weather == 803: '04d', 
              id_weather == 804: '04d', 
    }[True]

def export_html():
    SQL_wfc = Sqlite()
    rows = SQL_wfc.rows2export()
    html_rows = []
    for row in rows:
        id_city, name_city, date, temp, id_weather = row
        url_string = "http://openweathermap.org/img/w/{}.png".format(id_weather2png(id_weather))
        img_string = "<img src=\"{}\" />".format(url_string)
        row = id_city, name_city, date, temp, img_string
        print(row)
        html_rows.append(row)
    
    pd.set_option('display.max_colwidth', -1)
    df = pd.DataFrame(html_rows,columns='id_city name_city date temp id_weather'.split())
    with open(file_name, 'w') as filename:
        filename.write(df.head().to_html())

    with open(file_name, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace(r"&lt;", r"<")
    filedata = filedata.replace(r"&gt;", r">")
    with open(file_name, 'w') as file:
        file.write(filedata)


do = {
    "--csv": export_csv,
    "--json": export_json,
    "--html": export_html,
}

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    city_name = sys.argv[3]
except IndexError:
    city_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")