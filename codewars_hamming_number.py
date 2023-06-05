def hamming(n):
    res = [1] * n
    count2, count3, count5 = 0, 0, 0

    for i in range(1, n):
        res[i] = min(res[count2] * 2, res[count3] * 3, res[count5] * 5)
        if res[i] == res[count2] * 2:
            count2 += 1
        if res[i] == res[count3] * 3:
            count3 += 1
        if res[i] == res[count5] * 5:
            count5 += 1
    return res[-1]

print(hamming(4))