from typing import Tuple, Literal, Optional, TypedDict


PositionType = Tuple[int, int]
BlockMode = Optional[Literal["opposite", "wall"]]


class SideReturnType(TypedDict):
    counter: int
    blockMode: BlockMode
