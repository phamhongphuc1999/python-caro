import pytest

from CaroBoard.caro_win import CaroWin
from CaroBoard.utils import draw_list
from type import PositionType


@pytest.mark.parametrize(
    "board,current_player,position,expected",
    [
        (
            [
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 2, 1, 0],
                [0, 0, 2, 1, 0],
                [0, 0, 0, 1, 0],
            ],
            1,
            (0, 3),
            1,
        )
    ],
)
def test_check_win(
    board: list[list[int]], current_player: int, position: PositionType, expected: int
):
    counter = CaroWin.check_win(board, len(board), current_player, position)
    assert expected == counter
