from abc import ABC, abstractmethod

class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


class QuickSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using QuickSort")
        return sorted(data)


class MergeSort(SortingStrategy):
    def sort(self, data):
        print("Sorting using MergeSort")
        return sorted(data)


class DataProcessor:

    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def process(self, data):
        print(self.strategy.sort(data))


data = [3, 1, 4, 1, 5, 9]
processor = DataProcessor(QuickSort())
processor.process(data)


processor.set_strategy(MergeSort())
processor.process(data)