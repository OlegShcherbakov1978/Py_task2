import random
list_ = [1, 56, 4, 72, 23, 12, 8, 2, 43, 76, 27]
min = 5
max = 50

for i in range(len(list_)):
    if list_[i] > min and list_[i] < max:
        print(i, end=" ")
