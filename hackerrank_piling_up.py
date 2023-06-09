# deque. Why not?

from collections import deque

def loop(dq: deque, iterations: int) -> str:
    current = max(dq[0], dq[-1])
    for i in range(iterations):
        try:
            choice = max(i for i in (dq[0], dq[-1]) if i <= current)
        except ValueError:
            return 'No'
        if choice == dq[-1]:
            current = dq.pop()
        elif choice == dq[0]:
            current = dq.popleft()
    return 'Yes'


for i in range(int(input())):
    dq = deque()
    cubes_amount = int(input())
    [dq.append(int(i)) for i in input().split()]
    if dq:
        print(loop(dq, cubes_amount))
    else:
        print('No')
