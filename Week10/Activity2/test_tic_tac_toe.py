"""Unit tests for Tic-tac-toe game logic."""

import unittest

from tic_tac_toe import (
    EMPTY_CELL,
    PLAYER_O,
    PLAYER_X,
    create_board,
    format_board,
    get_winner,
    is_draw,
    is_game_over,
    is_valid_move,
    make_move,
    switch_player,
)


class TestTicTacToe(unittest.TestCase):
    """Test Tic-tac-toe board rules and helper functions."""

    def test_create_board_returns_empty_board(self) -> None:
        """A new board has nine empty cells."""
        board = create_board()

        self.assertEqual(len(board), 9)
        self.assertEqual(board, [EMPTY_CELL] * 9)

    def test_make_move_places_player_mark(self) -> None:
        """A valid move updates the selected board position."""
        board = create_board()

        make_move(board, 5, PLAYER_X)

        self.assertEqual(board[4], PLAYER_X)

    def test_make_move_rejects_occupied_position(self) -> None:
        """Players cannot move into an occupied cell."""
        board = create_board()
        make_move(board, 1, PLAYER_X)

        with self.assertRaises(ValueError):
            make_move(board, 1, PLAYER_O)

    def test_make_move_rejects_position_outside_board(self) -> None:
        """Players must choose positions from 1 to 9."""
        board = create_board()

        with self.assertRaises(ValueError):
            make_move(board, 10, PLAYER_X)

    def test_is_valid_move_returns_false_for_taken_cell(self) -> None:
        """A move is invalid when another mark already uses that cell."""
        board = create_board()
        make_move(board, 3, PLAYER_O)

        self.assertFalse(is_valid_move(board, 3))

    def test_switch_player_alternates_marks(self) -> None:
        """Turns alternate between X and O."""
        self.assertEqual(switch_player(PLAYER_X), PLAYER_O)
        self.assertEqual(switch_player(PLAYER_O), PLAYER_X)

    def test_get_winner_detects_row_win(self) -> None:
        """Three matching marks in a row wins the game."""
        board = [
            PLAYER_X,
            PLAYER_X,
            PLAYER_X,
            EMPTY_CELL,
            EMPTY_CELL,
            EMPTY_CELL,
            EMPTY_CELL,
            EMPTY_CELL,
            EMPTY_CELL,
        ]

        self.assertEqual(get_winner(board), PLAYER_X)

    def test_get_winner_detects_column_win(self) -> None:
        """Three matching marks in a column wins the game."""
        board = [
            PLAYER_O,
            EMPTY_CELL,
            EMPTY_CELL,
            PLAYER_O,
            PLAYER_X,
            EMPTY_CELL,
            PLAYER_O,
            EMPTY_CELL,
            PLAYER_X,
        ]

        self.assertEqual(get_winner(board), PLAYER_O)

    def test_get_winner_detects_diagonal_win(self) -> None:
        """Three matching marks diagonally wins the game."""
        board = [
            PLAYER_X,
            PLAYER_O,
            EMPTY_CELL,
            EMPTY_CELL,
            PLAYER_X,
            PLAYER_O,
            EMPTY_CELL,
            EMPTY_CELL,
            PLAYER_X,
        ]

        self.assertEqual(get_winner(board), PLAYER_X)

    def test_is_draw_returns_true_for_full_board_without_winner(self) -> None:
        """A full board with no winning line is a draw."""
        board = [
            PLAYER_X,
            PLAYER_O,
            PLAYER_X,
            PLAYER_X,
            PLAYER_O,
            PLAYER_O,
            PLAYER_O,
            PLAYER_X,
            PLAYER_X,
        ]

        self.assertTrue(is_draw(board))
        self.assertTrue(is_game_over(board))

    def test_format_board_shows_available_positions(self) -> None:
        """Empty cells display their one-based board positions."""
        board = create_board()

        self.assertIn("1", format_board(board))
        self.assertIn("9", format_board(board))


if __name__ == "__main__":
    unittest.main()
