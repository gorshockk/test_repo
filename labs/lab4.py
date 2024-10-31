from abc import ABC, abstractmethod

#1
# Интерфейс стратегии сортировки
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# Стратегия: Сортировка пузырьком
class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        arr = data.copy()  # Копируем данные, чтобы не изменять оригинальный список
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


# Стратегия: Сортировка питона
class PythonSortStrategy(SortingStrategy):
    def sort(self, data):
        return sorted(data)

# Контекст
class SortContext:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort_data(self, data):
        return self._strategy.sort(data)

###########################################
'''data = [1,11,2,0,-1,9,7]

context = SortContext(BubbleSortStrategy())
print("Bubble Sort:", context.sort_data(data))

context.set_strategy(PythonSortStrategy())
print("Python Built-in Sort:", context.sort_data(data))
'''

#2

# Базовый класс Handler
class SupportHandler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    @abstractmethod
    def handle_request(self, request):
        if self._next_handler:
            return self._next_handler.handle_request(request)
        else:
            return "No one could handle the request."

# Обработчик базовой поддержки
class BasicSupport(SupportHandler):
    def handle_request(self, request):
        if request == "simple issue":
            return "Basic Support: Issue resolved at basic level."
        else:
            return super().handle_request(request)

# Обработчик поддержки уровня 2
class LevelTwoSupport(SupportHandler):
    def handle_request(self, request):
        if request == "moderate issue":
            return "Level 2 Support: Issue resolved at level 2."
        else:
            return super().handle_request(request)

'''
support_chain = BasicSupport(LevelTwoSupport())
requests = ["simple issue", "moderate issue", "unknown issue"]
for req in requests:
    result = support_chain.handle_request(req)
    print(f"Request: {req} => {result}")
'''
################################################################
#3
class Iter:
    @abstractmethod
    def __iter__(self):
        pass
    @abstractmethod
    def __next__(self):
        pass
class ListIterator(Iter):
    def __init__(self,data):
        self.data=data
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.data):
            res=self.data[self.index]
            self.index+=1
            return res
        else:
            raise StopIteration

a=[1,2,3,5]
test=ListIterator(a)
for i in test:
    print(i)
