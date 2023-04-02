song = 'пара-ра-рам рам-пам-папам па-ра-па-да'.split()
vowels = 'уеёыаояию'
sum_of_vow = []

for i in range(len(song)):
    sum = 0
    for j in song[i]:
        if j in vowels:
            sum += 1
    sum_of_vow.append(sum)

print('Парам пам-пам') if len(set(sum_of_vow)) == 1 else print('Пам парам')
