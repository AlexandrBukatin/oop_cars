# Реализуйте класс «Стадион».
# Необходимо хранить в полях класса:
# название стадиона, дату открытия, страну, город, вместимость.
# Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.
# К уже реализованному классу «Стадион» добавьте конструктор, 
# а также необходимые перегруженные методы.

class Stadium:
    def __init__(self, name, date, country, city, capacity):
        self.name =name #название стадиона
        self.date = date #дата открытия
        self.country = country #страна
        self.city = city #город
        self.capacity = capacity #вместимость

    def __str__(self)->str:
        return f"Stadium info: \n"\
            f"{self.__name};\n"\
            f"{self.__date};\n"\
            f"{self.__country};\n"\
            f"{self.__city};\n"\
            f"{self.__capacity};\n"
    
    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return f"{self.__name}"

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def date(self):
        return self.__date

    @date.getter
    def date(self):
        return f"{self.__date}"

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def country(self):
        return self.__country

    @country.getter
    def country(self):
        return f"{self.__country}"

    @country.setter
    def country(self, value):
        self.__country = value

    @property
    def city(self):
        return self.__city

    @city.getter
    def city(self):
        return f"{self.__city}"

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.getter
    def capacity(self):
        return f"{self.__capacity}"

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

stadium1 = Stadium(name='name - Wembley Stadium', date='date - 1872', country='country - England', city='city - London', capacity='capacity - 90,000')
stadium2 = Stadium(name='name - Old Trafford', date='date - 1910', country='country - England', city='city - Manchester', capacity='capacity - 74,994')
stadium3 = Stadium(name='name - Emirates Stadium', date='date - 2006', country='country - England', city='city - London', capacity='capacity - 60,704')
stadium4 = Stadium(name='name - King Power Stadium', date='date - 2002', country='country - England', city='city - Leicester', capacity='capacity - 32,312')
print(stadium1)
print(stadium2)
print(stadium3)
print(stadium4)