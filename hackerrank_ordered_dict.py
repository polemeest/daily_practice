from collections import OrderedDict

order = OrderedDict()

for i in range(int(input())):
   a = input().split()
   order[' '.join(a[:-1])] = order.get(' '.join(a[:-1]), 0) + int(a[-1])

for i, j in order.items():
   print(i, j)


'''
input:

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
'''

'''
output:

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''