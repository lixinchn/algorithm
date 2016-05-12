import sys


class SelectionSort():
    def __init__(self):
        self.data = [10, 14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 94, 65, 82, 45]

    def do(self):
        for i in range(len(self.data)):
            min_int = sys.maxint
            min_int_pos = -1
            for j in range(i, len(self.data)):
                if self.data[j] < min_int:
                    min_int = self.data[j]
                    min_int_pos = j
            self.data[i], self.data[min_int_pos] = self.data[min_int_pos], self.data[i]


if __name__ == '__main__':
    ss = SelectionSort()
    ss.do()
    print ss.data
