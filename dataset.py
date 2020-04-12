import os
from matplotlib import pyplot as plt

# array = os.listdir('B:\FLIC-full\images')
# n = int(input())
# os.startfile('B:\FLIC-full\images\%s' % array[n])

# class Datasett():
#     def __init__(self, path):
#         self.path = path
#         self.array = os.listdir(path)

#     def __getitem__(self, index):
#         return os.startfile(self.path + '\\' + self.array[index])

class Datasett():
    def __init__(self, path):
        self.path = path
        self.array = os.listdir(path)

    def __getitem__(self, index):
        img = plt.imread(self.path + '\\' + self.array[index])
        plt.imshow(img)
        plt.show()
        return 0

