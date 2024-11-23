
#proxy
class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")

class Proxy:
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy: Checking access before forwarding request.")
        self._real_subject.request()
        print("Proxy: Logging request after forwarding.")

# Example
real_subject = RealSubject()
proxy = Proxy(real_subject)

proxy.request()
###############################################################
#adapter

# target
class Target:
    def request(self):
        return "Target: The default behavior."

# Adaptee
class Adaptee:
    def specific_request(self):
        return "Adaptee: Specific behavior."

# adapter
class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.specific_request()

# Example
target = Target()
print(target.request())  # Target: The default behavior.

adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Adaptee: Specific behavior.
###########################################################
#Bridge
from abc import ABC, abstractmethod

# Реализация: разные способы рисования
class DrawingTool(ABC):
    @abstractmethod
    def draw(self, shape):
        pass

class Brush(DrawingTool):
    def draw(self, shape):
        print(f"Drawing {shape} with a brush")

class Pencil(DrawingTool):
    def draw(self, shape):
        print(f"Drawing {shape} with a pencil")

# Абстракция: разные виды форм
class Shape(ABC):
    def __init__(self, drawing_tool: DrawingTool):
        self.drawing_tool = drawing_tool

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        self.drawing_tool.draw("circle")

class Square(Shape):
    def draw(self):
        self.drawing_tool.draw("square")

# Создание объектов
brush = Brush()
circle = Circle(brush)
square = Square(brush)

circle.draw()  # Drawing circle with a brush
square.draw()  # Drawing square with a brush

# Смена инструмента
pencil = Pencil()
circle.drawing_tool = pencil
circle.draw()  # Drawing circle with a pencil