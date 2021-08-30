# Реализуйте класс «Книга».
# Необходимо хранить в полях класса:
# название книги, год выпуска, издателя, жанр, автора, цену.
# Реализуйте методы класса для ввода данных, вывода данных, 
# реализуйте доступ к отдельным полям через методы класса.
# К уже реализованному классу «Книга» добавьте конструктор,
# а также необходимые перегруженные методы

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.__name = name #название книги
        self.__year = year #год выпуска
        self.__publisher = publisher #издательство
        self.__genre = genre #жанр
        self.__author = author #автор книги
        self.__price = price #ценa

    def __str__(self)->str:
        return f"Book info: \n"\
            f"{self.__name};\n"\
            f"{self.__year};\n"\
            f"{self.__publisher};\n"\
            f"{self.__genre};\n"\
            f"{self.__author};\n"\
            f"{self.__price};\n"

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
    def year(self):
        return self.__year

    @year.getter
    def year(self):
        return f"{self.__year}"

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def publisher(self):
        return self.__publisher

    @publisher.getter
    def publisher(self):
        return f"{self.__publisher}"

    @publisher.setter
    def publisher(self, value):
        self.__publisher = value

    @property
    def genre(self):
        return self.__genre

    @genre.getter
    def genre(self):
        return f"{self.__genre}"

    @genre.setter
    def genre(self, value):
        self.__genre = value

    @property
    def author(self):
        return self.__author

    @author.getter
    def author(self):
        return f"{self.__author}"

    @author.setter
    def author(self, value):
        self.__author = value

    @property
    def price(self):
        return self.__price

    @price.getter
    def price(self):
        return f"{self.__price}"

    @price.setter
    def price(self, value):
        self.__price = value

book1 = Book(name='name - The Adventures of Sherlock Holmes', year='year - 14 October 1892', publisher= 'publisher - The Strand Magazine ', genre='genre - detective', author='author - Arthur Conan Doyle', price='price - 55$')
book2 = Book(name='name -  Hitchhiker’s Guide to the Galaxy', year='year - 2005 ', publisher= 'publisher -  BBC’s The Big Read ', genre='genre - comedy science fiction', author='author - Douglas Adams.', price='price - 60$')
print(book1)
print(book2)

