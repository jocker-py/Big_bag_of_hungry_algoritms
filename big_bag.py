"""
Задача на программирование: непрерывный рюкзак

Первая строка содержит количество предметов 1 <= n <=10^3
и вместимость рюкзака 0 <= W <= 2*10^6
Каждая из следующих n строк задаёт стоимость 0 <= c_i <= 2⋅10^6
и объём 0 < wi ≤ 2⋅10^6 предмета (n, W, c_i, w_i — целые числа).
Выведите максимальную стоимость частей предметов
(от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак,
с точностью не менее трёх
знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000
"""


def put_in_bag(store, bag):
    sum = 0
    for i in sorted(store.keys(), reverse=True):
        if store[i] >= bag:
            sum += (i * bag)
            break
        else:
            sum += (i * store[i])
            bag -= store[i]

    return "{:.3f}".format(sum)

store = {}

items, bag = [int(i) for i in input().split()]

for i in range(items):
    cost, weight = [i for i in input().split()]
    if weight == 0 or weight == "None" or cost == "None":
        weight = 1000000000000
        cost = 0

    cost, weight = float(cost), float(weight)
    c_i = cost / weight
    if not c_i in store:
        store.setdefault(c_i, weight)
    else:
        store[c_i] += weight
print(put_in_bag(store, bag))
