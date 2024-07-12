grid = [["-", "#", "-", "-", "#", "-"],
        ["#", "-", "-", "#", "-", "-"],
        ["#", "-", "#", "-", "-", "#"],
        ["-", "#", "-", "-", "#", "-"],
        ["-", "#", "-", "#", "-", "#"]]
def adj_mines(grid, row, col):
# This function is used to count the number of adjacent mines
# I have included the row and column as parameters so that the direction of counting will 
# remain the same regardless of the number of rows and columns
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    mines_count = 0
    # I created a variable called "mines_count" and set it to 0 so that it can increment
    for direction in directions:
        new_row = row + direction[0]
        new_column = col + direction[1]
        if 0 <= new_row < len(grid) and 0 <= new_column < len(grid[0]) and grid[new_row][new_column] == "#":
        # This line is to make sure that the programmes does not go out of bound while counting
            mines_count += 1
    return mines_count


def dash(grid):
    new_grid = [[cell for cell in row] for row in grid]
# To add the number of adjacent mines to the existing grid 
    for r in range(len(grid)):
        for c in range(len(grid[0])):
             if grid[r][c] == "-":
                mines_count = adj_mines(grid, r, c)
                new_grid[r][c] = str(mines_count)
                # If the character equals "-", that space will be replaced by the adjacent mine count
                # which is calculated by the adj_mines function above
    return new_grid
for row in dash(grid):
    print(row)
     



