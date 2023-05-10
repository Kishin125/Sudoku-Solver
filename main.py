size = 9


def findEmptySpaces(grid):
    for x in range(size):
        for y in range(size):
            if grid[x][y] == 0:
                return[x][y]
    return None

def printGrid(grid):
    for x in range(size):
        for y in range(size):
            print(grid[x][y], end=" ")
        print()

def check_Valid(grid, row, col, num):
    for x in range(size):
        if grid[row][x] == num:
            return False

    for x in range(size):
        if grid[x][col] == num:
            return False

    row_start = (row//3)
    col_start = (col//3)
    for x in range(row_start*3, row_start*3+3):
        for y in range(col_start*3, col_start*3 + 3):
            if grid[x][y] == num:
                return False
    return True

# Solve using backtracking, brute forcing each number until it works
def SudukoSolver(grid, row, col):

    if (row == size - 1 and col == size):
        return True
    if col == size:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return SudukoSolver(grid, row, col + 1)
    for num in range(1, size + 1, 1):

        if check_Valid(grid, row, col, num):

            grid[row][col] = num
            if SudukoSolver(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

# 0 mean the space is empty
if __name__ == '__main__':

    grid = [[0, 2, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 2, 0, 0, 0, 9],
            [0, 0, 0, 0, 9, 8, 5, 0, 6],
            [5, 0, 0, 3, 0, 9, 0, 4, 0],
            [3, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 9, 0, 4, 0, 0, 8, 0, 3],
            [0, 0, 0, 0, 3, 0, 0, 0, 0],
            [7, 0, 0, 0, 0, 1, 0, 0, 8],
            [0, 8, 0, 9, 7, 4, 0, 0, 0]]

    print('Starting grid')
    print(printGrid(grid))

    if (SudukoSolver(grid, 0, 0)):
        print('Solved grid')
        printGrid(grid)
    else:
        print("No solution")


