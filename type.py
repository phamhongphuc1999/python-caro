from typing import Tuple, Literal, Optional, TypedDict

EMPTY = 0
PLAYER1 = 1
PLAYER2 = 2

LEFT_HORIZONTAL = [0, -1]
RIGHT_HORIZONTAL = [0, 1]
UP_VERTICAL = [-1, 0]
DOWN_VERTICAL = [1, 0]
UP_LEFT = [-1, -1]
DOWN_RIGHT = [1, 1]
UP_RIGHT = [-1, 1]
DOWN_LEFT = [1, -1]

DIRECTION = [
    LEFT_HORIZONTAL,
    RIGHT_HORIZONTAL,
    UP_VERTICAL,
    DOWN_VERTICAL,
    UP_LEFT,
    UP_RIGHT,
    DOWN_LEFT,
    DOWN_RIGHT,
]

EVALUATION_DIRECTIONS = [
    (0, 1),  # horizontal
    (1, 0),  # vertical
    (1, 1),  # diagonal
    (1, -1),  # diagonal
]

EVALUATION_SCORES = {
    (5, 2): 10**9,  # five consecutive steps
    (4, 2): 100000,  # opened four steps
    (4, 1): 10000,  # block four steps
    (3, 2): 1000,  # opened three steps
    (2, 2): 100,  # opened two steps
}


PositionType = Tuple[int, int]
BlockMode = Optional[Literal["opposite", "wall"]]


class SideReturnType(TypedDict):
    counter: int
    blockMode: BlockMode
