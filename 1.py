# Реализуйте класс «Автомобиль».
# Необходимо хранить в полях класса:
# название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
# Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.
# К уже реализованному классу «Автомобиль» добавьте конструктор,
# а также необходимые перегруженные методы. 

class Car:
    def __init__(self, make, year, mark, volume, color, price):
        self.make = make 
        self.year = year
        self.mark = mark
        self.volume = volume
        self.color = color
        self.price = price

    def __str__(self)-> str:
        return f"Car info:\n{ self.make };\n{ self.mark};\n{self.year};\n{self.color};\n{self.volume};\n{self.price}.\n"

    def get_make(self):
        return f"{self.make}"

    def set_make(self, value):
        self.make = value

    def get_mark(self):
        return f"{self.mark}"

    def set_mark(self, value):
        self.mark = value

    def get_year(self):
        return f"{self.year}"

    def set_year(self, value):
        self.year = value

    def get_color(self):
        return f"{self.color}"

    def set_color(self, value):
        self.color = value

    def get_volume(self):
        return f"{self.volume}"

    def set_volume(self, value):
        self.volume = value

    def get_price(self):
        return f"{self. price}"

    def set_price(self, value):
        self.price = value

    
car = Car(make = 'make - BMW',year = 'year - 2020',mark = 'mark - X7',volume = 'volume - 15.l',color = 'color - Black',price = 'price - 80000$')
car2 = Car(make = 'make - Toyota',year = 'year - 2015',mark = 'mark - Camry',volume = 'volume - 8,5.l',color = 'color - Silver',price = 'price - 20000$')
print(car)
print(car2)


    
      
    



    