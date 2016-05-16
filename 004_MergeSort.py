import random


class MergeSort():
    def __init__(self):
        # self.data = [10, 14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 94, 65, 82, 45]
        self.data = []
        for i in range(10000):
            self.data.append(int(random.random() * 10000))

    def do(self):
        ret_data = []
        for value in self.data:
            ret_data.append(value)
        self.sort(self.data, ret_data, 0, len(self.data) - 1)
        return ret_data

    def sort(self, data, ret_data, low, high):
        if high <= low:
            return
        middle = low + (high - low) / 2
        self.sort(data, ret_data, low, middle)
        self.sort(data, ret_data, middle + 1, high)
        self.merge(data, ret_data, low, middle, high)

        
    def merge(self, data, ret_data, low, middle, high):
        for i in range(len(ret_data)):
            data[i] = ret_data[i]

        i, j, k = low, middle + 1, low
        while k <= high:
            if i > middle:
                ret_data[k] = data[j]
                j += 1
            elif j > high:
                ret_data[k] = data[i]
                i += 1
            elif data[i] <= data[j]:
                ret_data[k] = data[i]
                i += 1
            else:
                ret_data[k] = data[j]
                j += 1
            k += 1



if __name__ == '__main__':
    ms = MergeSort()
    ret_data = ms.do()
    print ret_data
