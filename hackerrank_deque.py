# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

deq = deque()

for i in range(int(input())):
    command = input().split()
    if command[0] == 'append':
        deq.append(command[1])
    elif command[0] == 'appendleft':
        deq.appendleft(command[1])
    elif command[0] == 'pop':
        deq.pop()
    elif command[0] == 'popleft':
        deq.popleft()
print(*deq)


'''EVAL is not the answer to everything.
AND it's dangerous'''