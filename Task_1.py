# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# #     Пример:

# # - 0,56 -> 11

# # мысли только поместить либо в список, либо в строку.
# список
number = list(input('введи число '))
number.remove('.')

result = 0

for i in number:
    i = int(i)
    result += i
print (result)

#строка
result = 0
number = input('введи число ')

for i in number:
    if (i == '.'):
        continue
    result += int(i)
    
print (result)
