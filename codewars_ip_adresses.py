def ips_between(start, end):
    log = [map(int, var) for var in zip(start.split('.'), end.split('.'))]
    res = [b - a for a, b in log][::-1]
    return sum([res[i] * (256**i) for i in range(4)][::-1])

print(ips_between("10.0.0.0", "10.0.0.50"))
print(ips_between("20.0.0.10", "20.0.1.0"))
print(ips_between('170.0.0.0', '170.1.0.0')) #65536


# def ips_between(start, end):
#     start = [int(i) for i in start.split('.')]
#     end = [int(i) for i in end.split('.')]
#     res = [b - a for a, b in zip(start, end)]
#     res = [res[i] * (256**i) for i in range(4)][::-1]
#     return abs(sum(res))


# start = [int(i) for i in start.split('.')]
# end = [int(i) for i in end.split('.')]
