
import urllib.request
import gzip
import json
import os
from sqlite import Sqlite 


class city():
    def __init__(self, country, id_city, name_city):
        self._country = country
        self._id_city = id_city
        self._name_city = name_city
   
    def country(self):
        return self._country
   
    def id_city(self):
        return self._id_city
           
    def name_city(self):
        return self._name_city
   
    def set_temp(self, temp):
        self._temp = temp
    def temp(self):
        return self._temp

    def set_date(self, date):
        self._date = date
    def date(self):
        return self.date

    def set_id_weather(self, id_weather):
        self._id_weather = id_weather        
    def id_weather(self):
        return self._id_weather

    def get_weather_for_city(self):
        with open('app.id', 'r') as appid_file:
            app_id=appid_file.read().replace('\n', '')
        url_string = "http://api.openweathermap.org/data/2.5/weather?id={}&units=metric&appid={}".format(self.id_city(),app_id)
        with urllib.request.urlopen(url_string) as url:
            data = json.loads(url.read().decode())

        self.set_id_weather(data["weather"][0]["id"])
        self.set_temp(data["main"]["temp"])

        SQL_wfc = Sqlite()
        SQL_wfc.create()
         
        if SQL_wfc.contain(self.id_city()):
           SQL_wfc.update(self.id_city(), self.name_city(), self.temp(), self.id_weather()) 
        else:
            SQL_wfc.insert(self.id_city(), self.name_city(), self.temp(), self.id_weather())
        SQL_wfc.print()


class openweather():
    def __init__(self):
        self._city_list = []
        self._country_list = []
        self._country = 'RU'
        
    def get_from_json(self):
        with gzip.open('city.list.json.gz', 'rb') as f:
            file_content = f.read()
        city_json = json.loads(file_content)
        for cjs in city_json:
            self._city_list.append(city(cjs["country"],cjs["id"],cjs["name"]))
            self._country_list.append(cjs["country"])
        set_country_list = set(self._country_list)
        self._country_list = list(set_country_list)


    def set_country(self, country):
        self._country = country

    def country(self):
        return self._country

    def country_list(self):
        return self._country_list

    def city_list(self):
        return self._city_list

    def city_list_of(self):
        city_list_of = []
        for city in self._city_list:
            if city.country() == str(self.country()):
                city_list_of.append(city)
        return city_list_of

    def print_city_list_of(self):
        print("City's of {}: ".format(self.country()))
        for city in self.city_list_of():
            print("ID: {}; Name: {}".format(city.id_city(), city.name_city()))

    def print_country_list(self):
        print("Countries from openweather DB:")
        for country in self.country_list():
            print(country)

    def parse(self):
        if not os.path.isfile('./city.list.json.gz'):
            urllib.request.urlretrieve('http://bulk.openweathermap.org/sample/city.list.json.gz', './city.list.json.gz')
        self.get_from_json()
        answer = ""
        while answer != "q":
            print("Please, enter 'g' for input Country, 'c' - City, 'q' - Quit")
            answer = input()
            if answer == 'q':
                print("Goodbye!")
                return
            elif answer == 'g':
                self.print_country_list()
                print("Please, enter country name:")
                answer = input()
                if self._country_list.__contains__(answer):
                    self._country = answer
                    self.select_city()
            elif answer == 'c':
                self.select_city()

    def select_city(self):
        self.print_city_list_of()
        print("Please, enter city name:")
        answer = input()
        for cur_city in self.city_list():
            if cur_city.name_city() == answer and cur_city.country() == self.country():
                cur_city.get_weather_for_city()

      

