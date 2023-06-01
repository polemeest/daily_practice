from itertools import product

def get_pins(observed):

    # creating a matrix and hash for data
    matrix = [[i for i in range(n, n+3)] for n in (1,4,7)] + [[None, 0, None]]
    dic = {}

    # adding data to a dictionary with sets of possible buttons
    for i in range(4):
        if i == 0:
            point_x = (0, 2)
        elif i == 1:
            point_x = (-1, 2)
        else:
            point_x = (-1, 1)
        for j in range(3):
            if j == 0:
                point_y = (0, 2)
            elif j == 1:
                point_y = (-1, 2)
            else:
                point_y = (-1, 1)
            dic[str(matrix[i][j])] = set([str(matrix[i + x][j]) for x in range(*point_x)] + [str(matrix[i][j + y]) for y in range(*point_y)])

    # removing excessed values
    del dic['None']
    dic['0'].remove('None')
    dic['8'].add('0')
    
    # filling a log with possible values for each button
    log = [''.join(string) for string in product(*(dic[i] for i in observed))]
    return log

get_pins('8')
get_pins('11')
get_pins('369')