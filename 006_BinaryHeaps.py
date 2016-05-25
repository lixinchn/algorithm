import random


class BinaryHeaps():
    def __init__(self):
        # self.data = [0, 10, 14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 65, 82, 45]
        self.data = [0, 10]
        self.N = len(self.data) - 1

    def is_empty(self):
        return self.N == 0

    def insert(self, num):
        self.data.append(num)
        self.N += 1
        self.swim()

    def del_max(self):
        if self.is_empty():
            return None
        max_num = self.data[1]
        self.data[1], self.data[self.N] = self.data[self.N], self.data[1]
        self.N -= 1
        self.sink()

    def swim(self):
        i = self.N
        while i / 2 > 0 and self.data[i] > self.data[i / 2]:
            self.data[i], self.data[i / 2] = self.data[i / 2], self.data[i]
            i /= 2

    def sink(self):
        i = 1
        while i <= self.N:
            j = 2 * i
            if j + 1 <= self.N and self.data[j] < self.data[j + 1]:
                j += 1

            if j <= self.N and self.data[i] < self.data[j]:
                self.data[j], self.data[i] = self.data[i], self.data[j]
                i = j
                continue

            break

    def print_data(self):
        output = ''
        for i in range(1, self.N + 1):
            output += str(self.data[i]) + ', '
        print output


if __name__ == '__main__':
    bh = BinaryHeaps()
    for num in [14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 65, 82, 45]:
        bh.insert(num)

    bh.print_data()

    bh.del_max()
    bh.print_data()