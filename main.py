import random

colors = ['red', 'blue', 'yellow', 'purple', 'orange']

# Initialize an empty set to store unique grids
unique_grids = set()

# Generate 120 unique grids
while len(unique_grids) < 120:
    # Initialize an empty 5x5 grid
    grid = [['' for _ in range(5)] for _ in range(5)]

    # Fill the first row with randomly selected colors
    random.shuffle(colors)
    for i in range(5):
        grid[0][i] = colors[i]

    # Fill the remaining rows
    for i in range(1, 5):
        # Randomly select a color for the first column
        remaining_colors = [c for c in colors if c not in [grid[j][0] for j in range(i)]]
        if not remaining_colors:
            break
        color = random.choice(remaining_colors)
        grid[i][0] = color

        # Fill the remaining cells in the row
        j = 1
        attempts = 0
        while True:
            used_colors = set(grid[i][:j]) | set(grid[k][j] for k in range(i))
            remaining_colors = [c for c in colors if c not in used_colors]
            if not remaining_colors:
                break
            color = random.choice(remaining_colors)
            grid[i][j] = color
            j += 1

            if j == 5:
                break

            # If we have made too many attempts, start over with a new first row
            if attempts > 10:
                break

            attempts += 1

        # If we were unable to fill the entire row, start over with a new first row
        else:
            break

    # Check if the grid is complete and unique
    if all(grid[i][j] for i in range(5) for j in range(5)):
        grid_str = '\n'.join([' '.join(row) for row in grid])
        if grid_str not in unique_grids:
            unique_grids.add(grid_str)

# Write the unique grids to a file
with open('unique_grids.txt', 'w') as f:
    for grid_str in unique_grids:
        f.write(grid_str + '\n\n')
