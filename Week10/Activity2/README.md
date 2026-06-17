# Two-Player Tic-tac-toe CLI

This activity implements a console-based Tic-tac-toe game for two players.

Players take turns choosing positions from 1 to 9. Player X starts first, then
turns alternate until one player has three marks in a row, column, or diagonal,
or the board is full and the game ends in a draw.

## Project Structure

- `main.py`: Runs the interactive command-line game.
- `tic_tac_toe.py`: Contains the game rules and board helper functions.
- `test_tic_tac_toe.py`: Contains unit tests for the game logic.

## How to Run

From this folder, run:

```bash
python main.py
```

## How to Test

Run the unit tests:

```bash
python -m unittest -v
```

Run Pylint:

```bash
pylint main.py tic_tac_toe.py test_tic_tac_toe.py
```

## Coding Style

The code is written to follow PEP 8 conventions:

- Small functions with single responsibilities.
- Descriptive names for modules, functions, constants, and variables.
- Module and function docstrings.
- Explicit validation for invalid moves.
- Separated game logic from command-line input/output so the rules can be
  tested automatically.
