import random


class MergeSortFromTop():
    def __init__(self):
        # self.data = [10, 14, 73, 25, 23, 13, 27, 94, 33, 39, 25, 59, 65, 82, 45]
        self.data = []
        for i in range(10000):
            self.data.append(int(random.random() * 10000))

    def do(self):
        gap = 1
        len_data = len(self.data)
        while gap < len_data:
            i = 0
            while i < len_data:
                self.merge(self.data, i, i + gap - 1, min(i + 2 * gap - 1, len_data - 1))
                i += 2 * gap
            gap *= 2
        return self.data

        
    def merge(self, data, low, middle, high):
        data_temp = []
        i, j, k = low, middle + 1, low
        while k <= high:
            if i > middle:
                data_temp.append(data[j])
                j += 1
            elif j > high:
                data_temp.append(data[i])
                i += 1
            elif data[i] <= data[j]:
                data_temp.append(data[i])
                i += 1
            else:
                data_temp.append(data[j])
                j += 1
            k += 1
        data[low:high + 1] = data_temp



if __name__ == '__main__':
    ms = MergeSortFromTop()
    ret_data = ms.do()
    print ret_data
