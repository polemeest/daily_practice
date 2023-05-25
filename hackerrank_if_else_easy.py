if __name__ == '__main__':
    n = int(input().strip())
    print('Weird' if n % 2 == 1 or 5 < n < 21 else 'Not Weird')


'''
Task
Given an integer, , perform the following conditional actions:

If  is odd, print 'Weird'
If  is even and in the inclusive range of 2 to 5, print 'Not Weird'
If  is even and in the inclusive range of 6 to 20, print 'Weird'
If  is even and greater than 20, print 'Not Weird'
'''