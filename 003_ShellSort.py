class ShellSort():
    def __init__(self):
        self.data = [10, 14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 94, 65, 82, 45]

    def do(self):
        data_len = len(self.data)
        gap = data_len / 2
        while gap > 0:
            for i in range(gap):
                j = i + gap
                while j < data_len:
                    k = j - gap
                    while k > 0:
                        if self.data[j] < self.data[k]:
                            self.data[j], self.data[k] = self.data[k], self.data[j]
                        k -= gap
                    j += gap
            gap /= 2


if __name__ == '__main__':
    ss = ShellSort()
    ss.do()
    print ss.data
