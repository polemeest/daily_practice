def print_door_mat(height: int, width: int) -> None:
    half = height // 2
    log = []
    for i in range(half):
        log.append(f'{".|." * (1 + 2 * i):-^{width}}')
    log.append(f'{"WELCOME":-^{width}}')
    log += reversed(log[:-1])
    for i in log:
        print(i)




    # for i in range(height):
    #     if i < half:
    #         print(f'{".|." * (1 + 2 * i):-^{width}}')
    #     elif i == half:
    #         print(f'{"WELCOME":-^{width}}')
    #     else:
    #         print(f'{".|." * (height - 2 * (i % (half + 1))):-^{width}}')



print_door_mat(11, 33)