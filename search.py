from random import randint

list = [] #создаем пустой список для сортировки пузырьком
k = 0

for i in range (0, 100): #цикл для добавления элементов в список
    a = randint(1, 1_000_000) #выбираем число
    list.append(a) #добавляем его в список

stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            change = list[i]
            list[i] = list[i+1]
            list[i+1] = change
            stop_flag = True

stop_flag = True
while stop_flag is True:
        stop_flag = False
        for i in range(0, len(list)-1):
            if list[i] == list[i+1]:
                list[i] -= 1
                stop_flag = True
print(len(list))
print(list)
a = int(input('Введите элемент, который хотите найти: '))

find = False
print('Линейный поиск:')
for i in range(0, len(list)):
    k += 1
    if a == list[i]:
        print(f'Элемент {a} находится в списке на месте c индексом {i}')
        print(f'Для линейного поиска понадобилось {k} иттераций')
        find = True
        break
if find == False:
    print(f'Элемент {a} не найден в списке')


center = list[len(list)//2]
if a == center:
    print()

elif a > center:
    for i in range(0, len(list)//2):
        list.remove(list[i])

elif a < center:
    for i in range(len(list)//2, len(list)+1):
        print(i)
        list.remove(list[i])

print(list)
