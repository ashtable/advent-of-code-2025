## Puzzle 1 – Dial Turns

Tiny helper for Advent of Code 2025 puzzle 1. It reads turn instructions (e.g., `R24`, `L38`) from `input.txt`, spins a 0–99 dial starting at index 50, counts every time the dial lands on zero, and prints the result.

### Running
- Ensure you have Python 3.13+ and `uv` installed.
- From `puzzle-1/`, run:
  ```bash
  uv run python main.py
  ```

### Input format
- `input.txt` lives beside `main.py`.
- One instruction per line: `R|L` followed by an integer amount.

### Linting / typing
- Ruff enforces linting and required annotations:
  ```bash
  uv run ruff check .
  ```
