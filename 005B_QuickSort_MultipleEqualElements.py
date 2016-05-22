import random


class QuickSortE():
    def __init__(self):
        self.data = [1, 3, 1, 2, 2, 1, 1, 2, 3, 2, 5, 2, 4, 2, 1, 3, 4]

    def do(self):
        low, high = 0, len(self.data) - 1
        self.sort(self.data, low, high)

    def sort(self, data, low, high):
        if low >= high:
            return
        i = low
        lt, gt = low, high
        flag = data[low]
        while i <= gt:
            if data[i] > flag:
                data[i], data[gt] = data[gt], data[i]
                gt -= 1
                continue
            if data[i] < flag:
                data[i], data[lt] = data[lt], data[i]
                i += 1
                lt += 1
                continue
            i += 1
        self.sort(data, low, lt - 1)
        self.sort(data, gt + 1, high)


        
if __name__ == '__main__':
    qse = QuickSortE()
    qse.do()
    print qse.data
