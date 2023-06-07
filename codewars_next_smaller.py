from itertools import permutations

# def next_smaller(n):
#     str_n = '.'.join(str(n)).split('.')
#     digit = [n - int(''.join(i)) for i in list(permutations(str_n, r=len(str_n))) if i[0] != '0' and int(''.join(i)) < n]
#     return n - min(digit) if digit else -1


# def next_smaller(n):
#     str_n = '.'.join(str(n)).split('.')
#     digits = [int(''.join(i)) for i in list(permutations(str_n, r=len(str_n))) if i[0] != '0' and int(''.join(i)) < n]
#     print(digits)

#     return max(digits) if digits else -1



def next_smaller(n):
    digit = str(n - 1)
    while len(str(n)) == len(digit):
        if all(digit) in str(n):
            return digit
        digit = str(int(digit) - 1)

    return -1





print(next_smaller(907))