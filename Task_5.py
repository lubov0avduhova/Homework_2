
import random


num = int(input('Введите число промежутков '))
list_num = [*range (-num, num +1)]
print(f'Первоначальный список: ', list_num)

for i in list_num:
    list_num[i] = random.randint(list_num[0], list_num[-1])

print (list_num)