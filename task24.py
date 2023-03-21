# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке...

list1 = []
max = 0

i = int(input('ввндите к-во кустов: '))

for k in range(i):
    list1.append(int(input(f'введите к-во ягод на {k+1} кусте: ')))

for k in range(1, i-1):
    if (list1[k]+list1[k-1]+list1[k+1]) > max:
        max = (list1[k]+list1[k-1]+list1[k+1])
if (list1[0]+list1[1]+list1[i-1]) > max:
    max = (list1[0]+list1[1]+list1[i-1])
else:
    if list1[i-1]+list1[i-2]+list1[0] > max:
        max = (list1[i-1]+list1[i-2]+list1[0])


print(list1)
print(max)
