def count_mines(grid):
    """
    Function to count the number of adjacent mines for each spot in the grid.
    
    Args:
    - grid (list of lists): The grid containing # for mines and - for mine-free spots.
    
    Returns:
    - grid_with_numbers (list of lists): The grid with numbers indicating the adjacent mines.
    """
    rows = len(grid)  # Get the number of rows in the grid
    cols = len(grid[0])  # Get the number of columns in the grid
    
    # Create a new grid to store the counts
    grid_with_numbers = []
    
    # Loop through each row in the grid
    for i in range(rows):
        # Create a new row for the grid with numbers
        row_with_numbers = []
        # Loop through each cell in the row
        for j in range(cols):
            # If the current cell contains a mine, append '#' to the new row
            if grid[i][j] == '#':
                row_with_numbers.append('#')
            else:
                # Otherwise, count the number of adjacent mines
                count = 0
                # Loop through adjacent cells (including diagonals)
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        # Skip the current cell itself
                        if x == 0 and y == 0:
                            continue
                        # Check if the adjacent cell is within the grid boundaries
                        if 0 <= i + x < rows and 0 <= j + y < cols:
                            # If the adjacent cell contains a mine, increment the count
                            if grid[i + x][j + y] == '#':
                                count += 1
                # Append the count to the new row
                row_with_numbers.append(count)
        # Append the new row to the grid with numbers
        grid_with_numbers.append(row_with_numbers)
    
    return grid_with_numbers

def print_grid(grid):
    """
    Function to print the grid.
    
    Args:
    - grid (list of lists): The grid to print.
    """
    for row in grid:
        print(' '.join(map(str, row)))

# Example usage:
grid = [
    ['#', '-', '-', '-', '#'],
    ['-', '-', '-', '-', '-'],
    ['-', '#', '-', '-', '-'],
    ['#', '-', '-', '#', '-'],
    ['-', '-', '#', '-', '#']
]

grid_with_numbers = count_mines(grid)
print_grid(grid_with_numbers)