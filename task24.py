# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке...

list1 = []
max = 0
i = int(input('ввндите к-во кустов: '))
for k in range(i):
    list1.append(int(input(f'введите к-во ягод на {k+1} кусте: ')))
for k in range(1, i-2):
    if (list1[k]+list1[k-1]+list1[k+1]) > max:
        max = (list1[k]+list1[k-1]+list1[k+1])
print(list1)
print(max)
