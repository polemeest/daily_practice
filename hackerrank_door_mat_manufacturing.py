# def print_door_mat(height: int, width: int) -> None:
#     half = height // 2
#     log = []
#     for i in range(half):
#         log.append(f'{".|." * (1 + 2 * i):-^{width}}')
#     log.append(f'{"WELCOME":-^{width}}')
#     log += reversed(log[:-1])
#     for i in log:
#         print(i)

def print_door_mat(height: int) -> None:
    width = height * 3
    for i in range(height // 2):
        print(f'{".|." * (1 + 2 * i):-^{width}}')
    print(f'{"WELCOME":-^{width}}')
    for i in range(height // 2 - 1, -1, -1):
        print(f'{".|." * (1 + 2 * i):-^{width}}')




    # for i in range(height):
    #     if i < half:
    #         print(f'{".|." * (1 + 2 * i):-^{width}}')
    #     elif i == half:
    #         print(f'{"WELCOME":-^{width}}')
    #     else:
    #         print(f'{".|." * (height - 2 * (i % (half + 1))):-^{width}}')



print_door_mat(55)