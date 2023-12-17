import pygame
import sys
from game_opt import player, window_opt, gridobj

# Initialize pygame
pygame.init()

# Constants
wopt = window_opt(60,10,(30,30,30),(200,200,200),(255,255,255))

# Set up the display
screen = pygame.display.set_mode((wopt.width, wopt.height))
pygame.display.set_caption("Grid Game")
font = pygame.font.SysFont("Arial", 30)


# Game variables
grid = [[0 for _ in range(wopt.grid_size)] for _ in range(wopt.grid_size)]
player01 = player(gridobj(None,None), gridobj(None,None), 0)

# Draw the grid function
def draw_grid(wopt):
    screen.fill(wopt.bg_color)
    for x in range(wopt.grid_size):
        for y in range(wopt.grid_size):
            rect = pygame.Rect(x * wopt.cell_size, y * wopt.cell_size, wopt.cell_size, wopt.cell_size)
            pygame.draw.rect(screen, wopt.grid_color, rect, 1)
            if grid[x][y] != 0:
                number_surface = font.render(str(grid[x][y]), True, wopt.font_color)
                screen.blit(number_surface, (x * wopt.cell_size + 10, y * wopt.cell_size + 10))

# Find grid number function
def find_grid_number(x, y):
    for i in range(wopt.grid_size):
        for j in range(wopt.grid_size):
            rect = pygame.Rect(i * wopt.cell_size, j * wopt.cell_size, wopt.cell_size, wopt.cell_size)
            if rect.collidepoint(x, y):
                return i, j
    return None

# Implement the logic of the game here
def updateData(playerID, x, y):
    selected_grid = find_grid_number(x, y)
    if playerID.last_grid.x is None and playerID.current_grid.x is None:
        last_grid = playerID.current_grid
        current_grid = selected_grid
    else:
        current_grid = last_grid =  playerID.current_grid
        # Horizontal and vertical movement
        if current_grid.x == selected_grid.x:
            # Down direction
            if current_grid.y < selected_grid.y:
                current_grid.y = current_grid.y + 3
            # Up direction
            elif current_grid.y > selected_grid.y:
                current_grid.y = current_grid.y - 3
        if current_grid.y == selected_grid.y:
            # Right direction
            if current_grid.x < selected_grid.x:
                current_grid.x = current_grid.x + 3
            # Left direction
            elif current_grid.x > selected_grid.x:
                current_grid.x = current_grid.x - 3
        # Diagonal movement
        if current_grid.x < selected_grid.x:
            # Down right direction
            if current_grid.y < selected_grid.y:
                current_grid.x = current_grid.x + 2
                current_grid.y = current_grid.y + 2
            # Up right direction
            elif current_grid.y > selected_grid.y:
                current_grid.x = current_grid.x + 2
                current_grid.y = current_grid.y - 2
        if current_grid.x > selected_grid.x:
            # Down left direction
            if current_grid.y < selected_grid.y:
                current_grid.x = current_grid.x - 2
                current_grid.y = current_grid.y + 2
            # Up left direction
            elif current_grid.y > selected_grid.y:
                current_grid.x = current_grid.x - 2
                current_grid.y = current_grid.y - 2
    # Update the grid
    current_number = playerID.current_number + 1
    return player(last_grid, current_grid, current_number)

# Function to write current number to the screen on the current grid
def write_to_screen(playerID,wopt):
    current_grid = playerID.current_grid
    current_number = playerID.current_number
    grid[current_grid[0]][current_grid[1]] = current_number
    x = current_grid[0] * wopt.cell_size
    y = current_grid[1] * wopt.cell_size
    text = font.render(str(current_number), True, wopt.font_color)
    screen.blit(text, (x, y))

# Game loop
running = True

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Find the current grid and current number
            player01 = updateData(player01, pos[0], pos[1])
            # Write the current number to the screen
            write_to_screen(player01,wopt)


    # Update game state here
    
    # Draw everything here
    draw_grid(wopt)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()