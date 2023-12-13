refrs = ['aoooooooooontooooon', 'a1n1t1o1n1']
code, infected = "anton", ''
for ind, refr in enumerate(refrs, 1):
    count, found = 0, 0
    for letter in code:
        try:
            curr = refr.index(letter, count)
            if curr >= count:
                count = curr
                found += 1
            else:
                break
        except ValueError:
            break
    if found == len(code):
        infected += str(ind) 
if infected:
    print(*infected)
    
'''    
for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break    
'''