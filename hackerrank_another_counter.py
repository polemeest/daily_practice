from collections import Counter

word = Counter('aabbbccde')

[print(*i) for i in sorted(word.most_common(), key=lambda x: (-x[1], x[0]))[:3]]
