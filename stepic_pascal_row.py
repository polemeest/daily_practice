from time import time

def pascal(num: int) -> list:
    ''' takes number of Pascal's triangle row and return list of it's numbers '''
    start1 = time()
    res = [[1] * (i + 1) for i in range(num + 1)]
    if num > 1:
        for i in range(2, num + 1):
            for j in range(1, len(res[i]) - 1):
                res[i][j] = sum((res[i - 1][j - 1], res[(i - 1)][j],))
    print(res[num])
    print(time() - start1)

    start2 = time()
    li = [1]
    for i in range(num):
        for j in range(len(li) - 1):
            li[j] = li[j] + li[j + 1]
        li.insert(0, 1)

    print(li)
    print(time() - start2)
    
pascal(4)