# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях. 

num = int(input('Введите число промежутков '))
list_num = [*range (-num, num +1)]
index = 1
position = None
i = ''

while (i != 'stop'):
    i = input('Введите число ')
    if (i != 'stop'):
        position = int(i)
        index *= list_num[position]

print(index)