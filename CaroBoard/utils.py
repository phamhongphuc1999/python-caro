def is_in_board(x: int, y: int, size: int):
    return 0 <= x < size and 0 <= y < size


def draw_list(board: list[list[int]], size: int):
    print("***************************")
    for row in range(size):
        for _ in range(2 * size):
            print(end="-")
        print()
        for column in range(size):
            print(board[row][column], end="|")
        print()
    print("***************************")
