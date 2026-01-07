from typing import Set
import pytest

from CaroBoard.minmax import MinmaxUtils
from type import PositionType


@pytest.mark.parametrize(
    "board,expected",
    [
        (
            [
                [0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
            ],
            [
                (0, 1),
                (0, 2),
                (0, 3),
                (1, 1),
                (1, 3),
                (3, 2),
                (3, 3),
                (3, 4),
                (4, 2),
                (4, 4),
            ],
        )
    ],
)
def test_check_win(board: list[list[int]], expected: Set[PositionType]):
    moves = MinmaxUtils.generate_candidate_moves(board, 1)
    print(moves)
