from collections import Counter, namedtuple

Purchase = namedtuple('Purchase', ['size', 'price'])
unused_variable = int(input())
shoes_list = Counter(map(int, input().split()))
daily_income = 0

for i in range(int(input())):
    purchase = Purchase(*tuple(map(int, input().split())))
    if shoes_list[purchase.size] > 0:
        daily_income += purchase.price
        shoes_list.subtract({purchase.size: 1})

print(daily_income)
