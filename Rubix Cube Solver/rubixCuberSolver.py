import random
import pygame
import os


#generate a matrix that represents a rubix cube
#each face is represented by a 3x3 matrix
#each face is represented by a color

cube = [[[0 for x in range(3)] for y in range(3)] for z in range(6)]

# Generate a matrix that represents a scrambled Rubik's cube
# Each face is represented by a 3x3 matrix
# Each face is represented by a unique color

# Define the colors for each face
colors = ['white', 'yellow', 'green', 'blue', 'red', 'orange']

# Assign each face a unique color
for i in range(6):
    for j in range(3):
        for k in range(3):
            cube[i][j][k] = colors[i]

# Define the possible moves for each face
moves = {
    'U': [[0, 0, 0], [0, 0, 1], [0, 0, 2], [2, 0, 0], [2, 0, 1], [2, 0, 2], [3, 0, 0], [3, 0, 1], [3, 0, 2], [4, 0, 0], [4, 0, 1], [4, 0, 2]],
    'D': [[0, 2, 0], [0, 2, 1], [0, 2, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2], [3, 2, 0], [3, 2, 1], [3, 2, 2], [4, 2, 0], [4, 2, 1], [4, 2, 2]],
    'L': [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 0, 0], [1, 1, 0], [1, 2, 0], [5, 0, 2], [5, 1, 2], [5, 2, 2], [2, 0, 2], [2, 1, 2], [2, 2, 2]],
    'R': [[0, 0, 2], [0, 1, 2], [0, 2, 2], [1, 0, 2], [1, 1, 2], [1, 2, 2], [5, 0, 0], [5, 1, 0], [5, 2, 0], [3, 0, 0], [3, 1, 0], [3, 2, 0]],
    'F': [[2, 0, 0], [2, 1, 0], [2, 2, 0], [1, 0, 2], [1, 0, 1], [1, 0, 0], [5, 2, 0], [5, 2, 1], [5, 2, 2], [0, 2, 2], [0, 1, 2], [0, 0, 2]],
    'B': [[3, 0, 2], [3, 1, 2], [3, 2, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [5, 0, 0], [5, 0, 1], [5, 0, 2], [0, 0, 0], [0, 1, 0], [0, 2, 0]]
}

# Perform 20 random moves to scramble the cube
for i in range(20):
    # Choose a random move
    move = random.choice(list(moves.keys()))
    # Rotate the chosen face
    face = moves[move]
    temp = [cube[face[j][0]][face[j][1]][face[j][2]] for j in range(12)]
    for j in range(12):
        cube[face[j][0]][face[j][1]][face[j][2]] = temp[(j-3)%12]

#Visually represent the scrambled cube
# Define the colors for each face
colors = {
    'white': (255, 255, 255),
    'yellow': (255, 255, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'red': (255, 0, 0),
    'orange': (255, 165, 0)
}

# Define the size of each square in the Rubik's cube
squareSize = 50
outlineSize = 1
faceSpace = 5

# Initialize Pygame
pygame.init()

# Set the size of the window
window_size = (3 * squareSize * 4 + 5 * faceSpace, 3 * squareSize * 3 + 2 * faceSpace)
screen = pygame.display.set_mode(window_size)

# Draw the Rubik's cube
for i in range(6):
    for j in range(3):
        for k in range(3):
            # Calculate the position of the square
            x = (i % 4) * squareSize * 3 + k * squareSize
            y = (i // 4) * squareSize * 3 + j * squareSize
            # Draw the square with the corresponding color
            pygame.draw.rect(screen, colors[cube[i][j][k]], (x, y, squareSize, squareSize))
            pygame.draw.rect(screen, (0, 0, 0), (x, y, squareSize, squareSize), outlineSize)

# Update the display
pygame.display.flip()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os.sys.exit()