from itertools import permutations
from collections import Counter

# def next_smaller(n):
#     str_n = '.'.join(str(n)).split('.')
#     digit = [n - int(''.join(i)) for i in list(permutations(str_n, r=len(str_n))) if i[0] != '0' and int(''.join(i)) < n]
#     return n - min(digit) if digit else -1


# def next_smaller(n):
#     str_n = '.'.join(str(n)).split('.')
#     digits = [int(''.join(i)) for i in list(permutations(str_n, r=len(str_n))) if i[0] != '0' and int(''.join(i)) < n]
#     print(digits)

#     return max(digits) if digits else -1



# def next_smaller(n):
#     digit = str(n - 1)
#     while len(str(n)) == len(digit):
#         if Counter(digit) == Counter(str(n)):
#             return digit
#         digit = str(int(digit) - 1)

#     return -1


def next_smaller(n):
    digit = [int(i) for i in str(n)]
    if len(digit) == 1 or digit == sorted(digit):
        return -1
    position = len(str(n)) - 1
    next_smallest = float('-Inf')

    for i in range(len(digit) - 1, 0, -1):
        if digit[i] < digit[i - 1]:
            position -= 1
            for j in range(position, len(digit)):
                if digit[j] < digit[position] and digit[j] > next_smallest:
                    next_smallest = digit[j]
                    next_ind = j
            digit[position], digit[next_ind] = digit[next_ind], digit[position]
            res = digit[:position + 1] + sorted(digit[position + 1:], reverse=True)
            return int(''.join(str(i) for i in res)) if res[0] != 0 else -1
        position -= 1
    return -1





# print(next_smaller(907))
# print(next_smaller(531))
# print(next_smaller(135))
# print(next_smaller(2071))
# print(next_smaller(414))
print(next_smaller(1234567908))