import numpy as np
import matplotlib.pyplot as plt

# Create a grid
grid_size = 100
grid = np.zeros((grid_size, grid_size))

# Oats placement
oats = [(20, 30), (50, 50), (80, 70)]

for oat in oats:
    grid[oat] = 1

# Initial slime position
slime = [(50, 50)]
grid[50, 50] = 2

def random_generation(grid, slime):
    randX = np.random.randint(0, grid_size)
    randY = np.random.randint(0, grid_size)
    newPos = (randX, randY)
    slime.append(newPos)
    grid[newPos] = 2
    return slime

def random_direction(grid, slime):
    # Get the last slime position
    last_pos = slime[-1]
    randDir = np.random.choice(['up', 'down', 'left', 'right'])
    if randDir == 'up':
        newPos = (last_pos[0], last_pos[1] + 1)
    elif randDir == 'down':
        newPos = (last_pos[0], last_pos[1] - 1)
    elif randDir == 'left':
        newPos = (last_pos[0] - 1, last_pos[1])
    elif randDir == 'right':
        newPos = (last_pos[0] + 1, last_pos[1])

    # Ensure the new position is within bounds
    newPos = (newPos[0] % grid_size, newPos[1] % grid_size)
    if grid[newPos] != 2:
        slime.append(newPos)
        grid[newPos] = 2  # Update the grid with the new slime position
    return slime

# Choose whether to use random_generation or random_direction
use_random_generation = True

# Simulation loop
for _ in range(1000):
    if use_random_generation:
        slime = random_generation(grid, slime)
    else:
        slime = random_direction(grid, slime)
    plt.imshow(grid, cmap='hot')
    plt.pause(0.0001)
plt.show()
