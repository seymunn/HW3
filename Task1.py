# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
maximum = int(input('Введите кол-во элементов списка: '))
user_num = int(input('Введите искомое число: '))
num_list = [random.randint(0, 100) for i in range(maximum)]
count = 0
print(num_list)

for i in range(maximum):
    if user_num == num_list[i]:
        count += 1
if count > 0:
    print(f'Искомое число встречатеся {count} раз')
else:
    find_num = num_list[0]
    for i in range(1, maximum):
        if abs(user_num - find_num) > abs(user_num - num_list[i]):
            find_num = num_list[i]

    print('Искомого числа нет в списке. Наиболее близкое по значению к нему:', find_num)
