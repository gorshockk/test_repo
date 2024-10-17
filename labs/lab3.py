import sqlite3
from abc import ABC, abstractmethod
'''
###1 номер
class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:#проверка на наличие обьекта класса Database
            cls._instance = super().__new__(cls)
            cls._instance._initialize(*args, **kwargs)
        return cls._instance

    def _initialize(self, db_name):#подключение к бд
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()

######################################################################
#2 номер



class Transport(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def deliver(self):
        transport = self.create_transport()
        print(f"Доставка осуществляется с помощью {transport.move()}")


class Taxi:
    def move(self):
        return "такси"



class TaxiTransport(Transport):
    def create_transport(self):
        return Taxi()



taxi_factory = TaxiTransport()

taxi_factory.deliver()  # Вывод: Доставка осуществляется с помощью такси
############################################################################
# номер 3

#интерфейсы кнопок и текста
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Textrow(ABC):
    @abstractmethod
    def text(self):
        pass
#кнопки и текстовые поля винды и мака
class WindowsButton(Button):
    def paint(self):
        return "paint windows button"

class MacButton(Button):
    def paint(self):
        return "paint Mac button"

class WindowsRow(Textrow):
    def text(self):
        return "windows writes text"

class MacRow(Textrow):
    def text(self):
        return "Mac writes text"

#интерфейс фабрики
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_text_row(self)->Textrow:
        pass

#фабрики windows and mac
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    def create_text_row(self) ->Textrow:
        return WindowsRow()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    def create_text_row(self) ->Textrow:
        return MacRow()

#клиентский код
def client_code(factory:GUIFactory):
    button=factory.create_button()
    text_row=factory.create_text_row()

    print(button.paint())
    print(text_row.text())


platform = "Windows"  # Или "Mac"

if platform == "Windows":
    factory = WindowsFactory()
else:
    factory = MacFactory()

client_code(factory)
'''
########################################
# 4 номер
# Продукт
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None

    def __str__(self):
        return f"House with {self.walls}, {self.roof}, and {self.windows}"

# Базовый строитель
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, material):
        self.house.walls = f"{material} walls"
        return self

    def build_roof(self, type_):
        self.house.roof = f"{type_} roof"
        return self

    def build_windows(self, number):
        self.house.windows = f"{number} windows"
        return self

    def build(self):
        return self.house

# Конкретные строители
class BrickHouseBuilder(HouseBuilder):
    def build_walls(self):
        return super().build_walls("brick")

class WoodHouseBuilder(HouseBuilder):
    def build_walls(self):
        return super().build_walls("wood")

# Директор
class HouseDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        return (self.builder
                .build_walls()
                .build_roof("gable")
                .build_windows(4)
                .build())

# Пример использования

brick_builder = BrickHouseBuilder()
wood_builder = WoodHouseBuilder()

director = HouseDirector(brick_builder)
brick_house = director.construct_house()
print(brick_house)  # Вывод: House with brick walls, gable roof, and 4 windows

director = HouseDirector(wood_builder)
wood_house = director.construct_house()
print(wood_house)  # Вывод: House with wood walls, gable roof, and 4 windows

