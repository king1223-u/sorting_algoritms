class Sorting:
    def __init__(self, lst: list):
        self.__lst = lst

    def insertion_sort(self):
        """
        сортировка вставками
        """
        for i in range(1, len(self.__lst)):
            key = self.__lst[i]
            j = i - 1
            while j >= 0 and key < self.__lst[j]:
                self.__lst[j + 1] = self.__lst[j]
                j -= 1
            self.__lst[j + 1] = key

    def show(self):
        print(self.__lst)

    def bubble_sort(self):
        """
        сортировка пузырьком
        """
        isSorting = True
        while isSorting:
            for i in range(0, len(self.__lst) - 1):
                if self.__lst[i] > self.__lst[i + 1]:
                    self.__lst[i], self.__lst[i + 1] = self.__lst[i + 1], self.__lst[i]
            isSorting = False
            for i in range(0, len(self.__lst) - 1):
                if self.__lst[i] > self.__lst[i + 1]:
                    isSorting = True

    def selection_sort(self):
        """
        сортировка выбором
        """
        for i in range(0, len(self.__lst)):
            min_num = self.__lst[i]
            index = i
            for j in range(i, len(self.__lst)):
                if self.__lst[j] < min_num:
                    min_num = self.__lst[j]
                    index = j
            self.__lst[i], self.__lst[index] = self.__lst[index], self.__lst[i]

    def quick_sort(self):
        """
        быстрая сортировка
        """
        self.__lst = self.__qsort()

    def __qsort(self):
        if len(self.__lst) < 2:
            return self.__lst
        else:
            pivot = self.__lst[0]
            less = Sorting([i for i in self.__lst[1:] if i < pivot])

            greater = Sorting([i for i in self.__lst[1:] if i > pivot])

            return less.__qsort() + [pivot] + greater.__qsort()

    def __heap(self, n, i):
        largest = i
        left = i * 2 + 1
        right = i * 2 + 2

        if left < n and self.__lst[left] > self.__lst[largest]:
            largest = left

        if right < n and self.__lst[right] > self.__lst[largest]:
            largest = right

        if largest != i:
            self.__lst[largest], self.__lst[i] = self.__lst[i], self.__lst[largest]
            self.__heap(n, largest)

    def heap_sort(self):
        """
        сортировка кучей
        """
        n = len(self.__lst)

        for i in range(n // 2 - 1, -1, -1):
            self.__heap(n, i)

        for j in range(n - 1, 0, -1):
            self.__lst[j], self.__lst[0] = self.__lst[0], self.__lst[j]
            self.__heap(j, 0)

    def merge_sort(self):
        """
        сортировка слиянием
        """
        self.__lst = self.__merge_sort()

    def __merge_sort(self):
        if len(self.__lst) == 1:
            return self.__lst
        middle = len(self.__lst) // 2
        right_list = Sorting(self.__lst[middle:])
        left_list = Sorting(self.__lst[:middle])
        return self.__merge(left_list.__merge_sort(), right_list.__merge_sort())

    def __merge(self, arr1, arr2):
        p1 = 0
        p2 = 0
        sorted_list = []
        while p1 <= len(arr1) - 1 and p2 <= len(arr2) - 1:
            if arr1[p1] < arr2[p2]:
                sorted_list.append(arr1[p1])
                p1 += 1
            elif arr1[p1] > arr2[p2]:
                sorted_list.append(arr2[p2])
                p2 += 1
            else:
                sorted_list.append(arr1[p1])
                p1 += 1
        if p1 == len(arr1):
            while p2 <= len(arr2) - 1:
                sorted_list.append(arr2[p2])
                p2 += 1
        elif p2 == len(arr2):
            while p1 <= len(arr1) - 1:
                sorted_list.append(arr1[p1])
                p1 += 1
        return sorted_list
