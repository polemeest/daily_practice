import time


def sum_of_intervals(intervals):
    start = time.time()
    intervals.sort()
    log = [intervals.pop(0)]
    while intervals:
        current = intervals.pop(0)
        for i, item in enumerate(log):
            if current[0] <= item[1]:
                log[i] = (item[0], max(item[1], current[1]))
                break
        else:
            log.append(current)
    end = time.time() - start
    return sum([len(range(*item)) for item in set(log)]), end


print(sum_of_intervals([(483, 490), (315, 498), (306, 307)]))
print(sum_of_intervals([(268, 462), (358, 484), (187, 369), (-430, -353), (-341, 411), (433, 485)]))

'''
Not mine solutions:


def sum_of_intervals(intervals):
    intervals.sort()
    lim,res=intervals[0][0],0
    for i in range(len(intervals)):
        res+=max(intervals[i][1],lim)-max(intervals[i][0],lim)
        lim=max(lim,intervals[i][1])
    return res


def sum_of_intervals(intervals):
    s, top = 0, float("-inf")
    for a,b in sorted(intervals):
        if top < a: top    = a
        if top < b: s, top = s+b-top, b
    return s
'''

''' Mine solutions: '''
# def check(intervals, log):
#     while intervals:
#         current = intervals.pop(0)
#         for i, item in enumerate(log):
#             if current[0] in range(*item) and current[1] in range(*item):
#                 break
#             elif current[0] in range(*item) and current[1] > item[1]:
#                 log[i][0] = current[1]
#                 break
#             elif current[0] < item[0] and current[1] in range(*item):
#                 log[i][1] = current[0]
#                 break
#         else:
#             log.append(list(current))
#     return log

#    # b = [intervals[::-1].pop()]
#    # log = []
#    # print(b)
#    # for i, item in enumerate(intervals):
#    #     # if not b:
#    #     #     b.append(item[0], item[1])
#    #     if item[0] in range(*b[len(b) - 1]) or item[0] < b[len(b) - 1][0] and item[1] > b[len(b) - 1][1]:
#    #         b[len(b) - 1] = [min(b[len(b) - 1][0], item[0]), max(b[len(b) - 1][1], item[1])]
#    #     else:
#    #         b.append((item[0], item[1]))
#
#
#    # return b
#
#
#    # [[log.append(i) for i in range(*item) if i not in log] for item in intervals]
#    # return len(log)
#
#
#    #     start = time.time()
#    # log = [intervals.pop(0)]
#    # # log = check(intervals, log)
#    # # ends = check(log, [[0,0]])
#    # while intervals:
#    #     current = intervals.pop(0)
#    #     for i, item in enumerate(log):
#    #         if current[0] in range(*item) and current[1] in range(*item):
#    #             break
#    #         elif (current[0] < item[0] and current[1] in range(*item)) or (current[0] in range(*item) and current[1] > item[1]):
#    #             log[i] = (min(current[0], item[0]), max(current[1], item[1]))
#    #             break
#    #         elif current[0] <= item[0] and current[1] >= item[1]:
#    #             log[i] = item
#    #     else:
#    #         log.append(current)
#    # logs = {s for s in log if log.count(s) == 1}
#    # print(log)
#    # print(logs)
#    # end = time.time() - start
#    # return sum([len(range(*item)) for item in set(logs)]), end