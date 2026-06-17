"""Command-line interface for a two-player Tic-tac-toe game."""

from tic_tac_toe import (
    PLAYER_O,
    PLAYER_X,
    create_board,
    format_board,
    get_winner,
    is_draw,
    make_move,
    switch_player,
)


def main() -> None:
    """Run the interactive two-player Tic-tac-toe game."""
    board = create_board()
    current_player = PLAYER_X

    print("Two-Player Tic-tac-toe")
    print("Player 1 uses X. Player 2 uses O.")
    print("Choose a board position from 1 to 9.")

    while True:
        print()
        print(format_board(board))

        position = ask_for_position(current_player)

        try:
            make_move(board, position, current_player)
        except ValueError as error:
            print(f"Invalid move: {error}")
            continue

        winner = get_winner(board)
        if winner is not None:
            print()
            print(format_board(board))
            print(f"Player {winner} wins.")
            break

        if is_draw(board):
            print()
            print(format_board(board))
            print("The game is a draw.")
            break

        current_player = switch_player(current_player)


def ask_for_position(player: str) -> int:
    """Ask the current player for a board position."""
    player_name = get_player_name(player)
    user_input = input(f"{player_name}, enter position: ").strip()

    try:
        return int(user_input)
    except ValueError:
        return 0


def get_player_name(player: str) -> str:
    """Return the display name for a player's mark."""
    if player == PLAYER_X:
        return "Player 1 (X)"
    if player == PLAYER_O:
        return "Player 2 (O)"
    return f"Player {player}"


if __name__ == "__main__":
    main()
