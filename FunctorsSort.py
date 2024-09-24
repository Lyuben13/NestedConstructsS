from abc import ABC, abstractmethod


# Интерфейс за стратегията
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass


# Имплементация на MergeSort стратегията
class MergeSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Data is Merge sorted")
        return sorted(data)  # Примерна имплементация на Merge Sort (тук е опростено)


# Имплементация на HeapSort стратегията
class HeapSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Data is Heap sorted")
        return sorted(data)  # Примерна имплементация на Heap Sort (тук е опростено)


# Имплементация на QuickSort стратегията
class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        print("Data is Quick sorted")
        return sorted(data)  # Примерна имплементация на Quick Sort (тук е опростено)


# Клас, който избира стратегията
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, data):
        return self._strategy.sort(data)


# Клиентски код
data = [34, 7, 23, 32, 5, 62]

# Използване на MergeSort
sorter = Sorter(MergeSortStrategy())
sorted_data = sorter.sort(data)
print(f"Sorted data using MergeSort: {sorted_data}")

# Превключване към QuickSort
sorter.set_strategy(QuickSortStrategy())
sorted_data = sorter.sort(data)
print(f"Sorted data using QuickSort: {sorted_data}")

# Превключване към HeapSort
sorter.set_strategy(HeapSortStrategy())
sorted_data = sorter.sort(data)
print(f"Sorted data using HeapSort: {sorted_data}")
