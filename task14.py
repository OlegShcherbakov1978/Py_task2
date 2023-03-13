# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

import math
n = int(input("N: "))
for i in range(int(math.log(n, 2))+1):
    print(2**i)
