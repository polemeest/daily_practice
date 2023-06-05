def recoverSecret(triplets):
    if not triplets:
        return triplets
    log = []
    [[log.append(i) for i in triplet if i not in log] for triplet in triplets]

    change = True
    while change:
        change = False

        for triplet in triplets:
            first = log.index(triplet[0])
            second = log.index(triplet[1])
            third = log.index(triplet[2])

            if first != min(first, second, third) or third != max(first, second, third):
                change = True

                median_hook = first + second + third
                first = min(first, second, third)
                third = max(first, second, third)
                second = median_hook - (first + third)

                log[first] = triplet[0]
                log[second] = triplet[1]
                log[third] = triplet[2]

    return ''.join(log)

print(recoverSecret([
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]))