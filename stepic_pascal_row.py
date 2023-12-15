def pascal(num: int) -> list:
    ''' takes number of Pascal's triangle row and return list of it's numbers '''
    res = [[1 for i in range(1, j + 1)] for j in range(1, num + 1)]
    if num > 1:
        for ind, lst in enumerate(res):
            for index, number in enumerate(lst):
                None
    
    return res[num]

print(pascal(0))