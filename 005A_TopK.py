import random


class TopK():
    def __init__(self):
        self.data = [10, 14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 65, 82, 45]
        # self.data = []
        # for i in range(10000):
        #     self.data.append(int(random.random() * 10000))

    def do(self, k):
        k = k - 1
        low, high = 0, len(self.data) - 1
        while True:
            index = self.partition(self.data, low, high)
            if index < k:
                low = index + 1
                continue
            if index > k:
                high = index - 1
                continue
            return self.data[index]

        
    def partition(self, data, low, high):
        flag = low
        while low <= high:
            while low <= high and data[low] <= data[flag]:
                low += 1
            while low <= high and data[high] >= data[flag]:
                high -= 1
            if low > high:
                data[high], data[flag] = data[flag], data[high]
                return high
            data[low], data[high] = data[high], data[low]
        return -1


if __name__ == '__main__':
    tk = TopK()
    ret = tk.do(7)
    print ret
