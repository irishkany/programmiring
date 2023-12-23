import pathlib
import typing as tp
from random import randint

T = tp.TypeVar("T")

def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)




def display(grid: tp.List[tp.List[str]]) -> None:
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()

def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    grid = []
    for i in range(n):
        grid.append(values[n * i:n * (i + 1)])
    return grid

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    return grid[pos[0]]

def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    col_number = pos[1]
    col = []
    for row in grid:
        col.append(row[col_number])
    return col

def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    n = int(len(grid) ** 0.5)
    block_row_number, block_col_number = pos[0] // n, pos[1] // n
    block = []
    for i in range(block_row_number * n, (block_row_number + 1) * n):
        for j in range(block_col_number * n, (block_col_number + 1) * n):
            block.append(grid[i][j])
    return block




def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    def get_solution(sudoku: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
        empty_position = find_empty_positions(sudoku)
        if empty_position is None:
            return sudoku
        possible_values = find_possible_values(sudoku, empty_position)
        if not possible_values:
            return None
        row_empty_position, col_empty_position = empty_position
        for i in possible_values:
            sudoku[row_empty_position][col_empty_position] = i
            if get_solution(sudoku) is not None:
                return sudoku
            sudoku[row_empty_position][col_empty_position] = "."
        return None
    return get_solution(grid)

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    if not solution:
        return False
    n = len(solution)
    for row in solution:
        if '.' in row:
            return False
        for i in row:
            if row.count(i) > 1:
                return False
    for i in range(n):
        col = get_col(solution, (0, i))
        for j in col:
            if col.count(j) > 1:
                return False
    block_len = int(n ** 0.5)
    for i in range(block_len):
        for j in range(block_len):
            block = get_block(solution, (i * block_len, j * block_len))
            for k in block:
                if block.count(k) > 1:
                    return False
    return True




if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        print(grid)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
