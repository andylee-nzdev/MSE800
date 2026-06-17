"""Core game logic for a two-player Tic-tac-toe CLI."""

from __future__ import annotations

from typing import Final

BOARD_SIZE: Final[int] = 9
WINNING_LINES: Final[tuple[tuple[int, int, int], ...]] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)
PLAYER_X: Final[str] = "X"
PLAYER_O: Final[str] = "O"
EMPTY_CELL: Final[str] = " "


def create_board() -> list[str]:
    """Create an empty Tic-tac-toe board."""
    return [EMPTY_CELL] * BOARD_SIZE


def format_board(board: list[str]) -> str:
    """Return a readable board display for the CLI."""
    rows = []

    for row_index in range(0, BOARD_SIZE, 3):
        row = [
            board[row_index + offset]
            if board[row_index + offset] != EMPTY_CELL
            else str(row_index + offset + 1)
            for offset in range(3)
        ]
        rows.append(f" {row[0]} | {row[1]} | {row[2]} ")

    return "\n---+---+---\n".join(rows)


def is_valid_move(board: list[str], position: int) -> bool:
    """Check whether a one-based board position is available."""
    return 1 <= position <= BOARD_SIZE and board[position - 1] == EMPTY_CELL


def make_move(board: list[str], position: int, player: str) -> None:
    """Place a player's mark on the board.

    Raises:
        ValueError: If the position is outside the board or already occupied.
    """
    if player not in (PLAYER_X, PLAYER_O):
        raise ValueError("Player must be X or O.")

    if not is_valid_move(board, position):
        raise ValueError("Move must be an empty position from 1 to 9.")

    board[position - 1] = player


def switch_player(current_player: str) -> str:
    """Return the next player mark."""
    if current_player == PLAYER_X:
        return PLAYER_O
    return PLAYER_X


def get_winner(board: list[str]) -> str | None:
    """Return the winning player, or None when there is no winner."""
    for first, second, third in WINNING_LINES:
        mark = board[first]
        if mark != EMPTY_CELL and mark == board[second] == board[third]:
            return mark

    return None


def is_draw(board: list[str]) -> bool:
    """Return True when the board is full and neither player has won."""
    return get_winner(board) is None and EMPTY_CELL not in board


def is_game_over(board: list[str]) -> bool:
    """Return True when the game has a winner or a draw."""
    return get_winner(board) is not None or is_draw(board)
