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
        data = []
        i, j, k = low, middle + 1, low
        while k <= high:
            if i > middle:
                data.append(ret_data[j])
                j += 1
            elif j > high:
                data.append(ret_data[i])
                i += 1
            elif ret_data[i] <= ret_data[j]:
                data.append(ret_data[i])
                i += 1
            else:
                data.append(ret_data[j])
                j += 1
            k += 1
        ret_data[low:high + 1] = data



if __name__ == '__main__':
    ms = MergeSort()
    ret_data = ms.do()
    print ret_data
