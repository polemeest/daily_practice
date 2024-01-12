word = 'a b c d'.split()
res = [] 
l = r = 0
for r, let in enumerate(word):
    if let != word[l]:
        res.append(word[l:r])
        l = r
res.append(word[l::])
print(res)