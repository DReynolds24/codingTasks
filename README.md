# Coding Tasks

This repository contains various coding tasks including the Minesweeper game.

## Minesweeper

Minesweeper is a puzzle game where the objective is to clear a rectangular board containing hidden 
"mines" without detonating any of them, 
with help from clues about the number of neighboring mines in each field.

### How to Play

- The board is divided into cells, each of which can either be empty or contain a mine.
- The player selects a cell to reveal its content.
- If a cell containing a mine is revealed, the game is over.
- If an empty cell is revealed, a number is displayed indicating how many adjacent cells contain mines.
- The player wins by revealing all non-mine cells.

### Features

- Randomly generated minefield.
- User-friendly interface to select cells.
- Displays the number of mines adjacent to each cell.

### How to Run

To run the Minesweeper game, execute the following command:

```sh
python minesweeper.py
