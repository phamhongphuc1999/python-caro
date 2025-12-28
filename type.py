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


PositionType = Tuple[int, int]
BlockMode = Optional[Literal["opposite", "wall"]]


class SideReturnType(TypedDict):
    counter: int
    blockMode: BlockMode
