class BubbleSortBidirectional:
    def __init__(self, a):
        self.__a = a
        self.__nItems = len(a)

    def swap(self, i, j):
        self.__a[i], self.__a[j] = self.__a[j], self.__a[i]

    def bubbleSort(self):
        left = 0
        right = self.__nItems - 1
        while left < right:
            for i in range(left, right):
                if self.__a[i] > self.__a[i + 1]:
                    self.swap(i, i + 1)
            right -= 1
            for i in range(right, left, -1):
                if self.__a[i] < self.__a[i - 1]:
                    self.swap(i, i - 1)
            left += 1

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorter = BubbleSortBidirectional(arr)
    sorter.bubbleSort()
    print("Array ordenado", sorter._BubbleSortBidirectional__a)