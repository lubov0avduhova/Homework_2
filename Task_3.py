#Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

# как я поняла задачу :
# 1. к - чисел вводит пользователь
# 2. в списке создается количество "мест" на количество чисел 1 пункта
# 3. в эти места с помощью range вставляются числа от 1 до k
# 4. каждое место вычисляется с помощью формулы
# 5. то, что получилось в формуле мы складываем между собой


k = int(input('Введите число: '))
num_of_list = [*range(1,k + 1)]
sum = 0

for i in num_of_list:
    sum += ((1 + 1/i)**i)

print(sum)



