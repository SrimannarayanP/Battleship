import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 9
CELL_SIZE = 40  # Adjust this based on your preferences
GRID_WIDTH = GRID_SIZE * CELL_SIZE
GRID_HEIGHT = GRID_SIZE * CELL_SIZE
GRID_SPACING = 50
RED_BORDER_SIZE = 5
GREEN_BORDER_SIZE = 40# Increased border size for the red border
BLACK_BORDER_SIZE = 2
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)  # New color for the ship
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

screen_width = 1260
screen_height = 960

# Create the screen
# screen_width = 2 * (GRID_WIDTH + RED_BORDER_SIZE * 2 + GRID_SPACING)
# screen_height = 2 * (30 + GRID_HEIGHT + RED_BORDER_SIZE * 2)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Two Blue Grids")

# Set up font
font = pygame.font.Font(None, 36)

# Battleship variables
ship_length = 3
player_ship_position = (0, 0)
player_ship_orientation = "horizontal"
opponent_ship_position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - ship_length))
opponent_ship_orientation = random.choice(["horizontal", "vertical"])
player_guess = None


# Draw a single grid
def draw_grid(color, border_size, offset_y):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x = border_size + col * CELL_SIZE + border_size * (col + 1)
            y = offset_y + border_size + row * CELL_SIZE + border_size * (row + 1)
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

# Draw your ship
'''def draw_ship(color, border_size, offset_y):
    for i in range(ship_length):
        x = offset_x + border_size + (player_ship_position[1] + i) * CELL_SIZE + border_size * (player_ship_position[1] + i + 1)
        y = offset_y + border_size + player_ship_position[0] * CELL_SIZE + border_size * (player_ship_position[0] + 1)
        pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))'''
def draw_ship(color, border_size, offset_y):
    for i in range(ship_length):
        x = offset_x + border_size + (player_ship_position[1] + i) * CELL_SIZE + border_size * (player_ship_position[1] + i + 1)
        y = offset_y + border_size + player_ship_position[0] * CELL_SIZE + border_size * (player_ship_position[0] + 1)
        pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))


# Draw the opponent's ship
def draw_opponent_ship(color, border_size, offset_y):
    for i in range(ship_length):
        x = offset_x + border_size + (opponent_ship_position[1] + i) * CELL_SIZE + border_size * (opponent_ship_position[1] + i + 1)
        y = offset_y + border_size + opponent_ship_position[0] * CELL_SIZE + border_size * (opponent_ship_position[0] + 1)
        pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

# Define the initial position and size of the player's ship
player_ship_orientation = "horizontal"  # Initial orientation
player_ship_position = (0, 0)
player_ship_color = (255, 165, 0)  # Orange color for the ship

# Define the Rotate button properties
rotate_button_rect = pygame.Rect(10, 10, 100, 40)
rotate_button_color = (0, 128, 255)
font = pygame.font.Font(None, 36)

def rotate_player_ship():
    global player_ship_orientation
    player_ship_orientation = "vertical" if player_ship_orientation == "horizontal" else "horizontal"




# Main loop
'''show_rotate_button = True  # Initial state
show_start_button = True   # Initial state
game_started = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check left mouse button click
            mouse_x, mouse_y = event.pos
            # Check if the mouse click is within the bounds of the Start button
            if show_start_button and start_button_rect.collidepoint(mouse_x, mouse_y):
                 # Rotate the player's ship
                player_ship_orientation = "vertical" if player_ship_orientation == "horizontal" else "horizontal"
            elif show_start_button and start_button_rect.collidepoint(mouse_x, mouse_y):
                # Start the game
                game_started = True
            elif not game_started:
                # Place the player's ship
                row = (mouse_y - offset_y - RED_BORDER_SIZE) // (CELL_SIZE + BLACK_BORDER_SIZE)
                col = (mouse_x - offset_x - RED_BORDER_SIZE) // (CELL_SIZE + BLACK_BORDER_SIZE)

                if player_ship_orientation == "horizontal" and col + ship_length <= GRID_SIZE:
                    player_ship_position = (row, col)
                elif player_ship_orientation == "vertical" and row + ship_length <= GRID_SIZE:
                    player_ship_position = (row, col)'''
# Main loop 2
'''show_rotate_button = True  # Initial state
show_start_button = True   # Initial state
game_started = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check left mouse button click
            mouse_x, mouse_y = event.pos
            # Check if the mouse click is within the bounds of the Start button
            if show_rotate_button and rotate_button_rect.collidepoint(mouse_x, mouse_y):
                # Rotate the player's ship
                player_ship_orientation = "vertical" if player_ship_orientation == "horizontal" else "horizontal"
            elif show_start_button and start_button_rect.collidepoint(mouse_x, mouse_y):
                # Start the game
                game_started = True
            elif not game_started:
                # Place the player's ship
                row = (mouse_y - offset_y - RED_BORDER_SIZE) // (CELL_SIZE + BLACK_BORDER_SIZE)
                col = (mouse_x - offset_x - RED_BORDER_SIZE) // (CELL_SIZE + BLACK_BORDER_SIZE)

                if player_ship_orientation == "horizontal" and col + ship_length <= GRID_SIZE:
                    player_ship_position = (row, col)
                elif player_ship_orientation == "vertical" and row + ship_length <= GRID_SIZE:
                    player_ship_position = (row, col)'''

def target_square(row, col):
    rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, RED, rect, 1)

# Main loop 3
show_rotate_button = True  # Initial state
show_start_button = True   # Initial state
game_started = False
'''while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check left mouse button click
            mouse_x, mouse_y = event.pos
            # Check if the mouse click is within the bounds of the Rotate button
            if show_rotate_button and rotate_button_rect.collidepoint(mouse_x, mouse_y):

                # Rotate the player's ship
                player_ship_orientation = "vertical" if player_ship_orientation == "horizontal" else "horizontal"

            elif show_start_button and start_button_rect.collidepoint(mouse_x, mouse_y):
                # Start the game
                game_started = True
            elif not game_started:
                # Place the player's ship
                row = (mouse_y - offset_y - RED_BORDER_SIZE) // (CELL_SIZE + BLACK_BORDER_SIZE)
                col = (mouse_x - offset_x - RED_BORDER_SIZE) // (CELL_SIZE + BLACK_BORDER_SIZE)

                if player_ship_orientation == "horizontal" and col + ship_length <= GRID_SIZE:
                    player_ship_position = (row, col)
                elif player_ship_orientation == "vertical" and row + ship_length <= GRID_SIZE:
                    player_ship_position = (row, col)'''
#Main loop 4
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            if rotate_button_rect.collidepoint(mouse_x, mouse_y):
                rotate_player_ship()
            elif show_start_button and start_button_rect.collidepoint(mouse_x, mouse_y):
                game_started = True
            elif not game_started:
                row = (mouse_y - offset_y - RED_BORDER_SIZE) // (CELL_SIZE + BLACK_BORDER_SIZE)
                col = (mouse_x - offset_x - RED_BORDER_SIZE) // (CELL_SIZE + BLACK_BORDER_SIZE)

                if player_ship_orientation == "horizontal" and col + ship_length <= GRID_SIZE:
                    player_ship_position = (row, col)
                elif player_ship_orientation == "vertical" and row + ship_length <= GRID_SIZE:
                    player_ship_position = (row, col)

    # Rest of your game loop code...


    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the red border for the first set of grids
    #pygame.draw.rect(screen, RED, (0, 0, screen_width, GRID_HEIGHT + RED_BORDER_SIZE * 2))

    # Draw the blue grid for the first set
    '''draw_grid(BLUE, BLACK_BORDER_SIZE, RED_BORDER_SIZE)'''
    offset_x = 0
    offset_y = RED_BORDER_SIZE
    draw_grid(BLUE, BLACK_BORDER_SIZE, offset_y)

    # Draw the red border for the second set of grids
    #pygame.draw.rect(screen, RED, (0, GRID_HEIGHT + RED_BORDER_SIZE * 2 + GRID_SPACING, screen_width, GRID_HEIGHT + RED_BORDER_SIZE * 2))

    # Draw the blue grid for the second set
    draw_grid(BLUE, BLACK_BORDER_SIZE, GRID_HEIGHT + RED_BORDER_SIZE * 2 + GRID_SPACING + RED_BORDER_SIZE)

    # Draw text on the right side
    text = font.render("Hello, welcome to my game", True, BLACK)
    text_rect = text.get_rect(center=(screen_width - 250, screen_height // 20))
    screen.blit(text, text_rect)

    # GREEN BORDER CENTRE
    pygame.draw.rect(screen,GREEN, (screen_width // 2 - GREEN_BORDER_SIZE // 2 - 18, 0, GREEN_BORDER_SIZE, screen_height))

    # Draw the player's ship
    draw_ship(ORANGE, BLACK_BORDER_SIZE, offset_y)

    # Draw the opponent's ship (only if the game has started)
    if game_started:
        draw_opponent_ship(ORANGE, GRID_WIDTH + 2 * RED_BORDER_SIZE + 2 * GRID_SPACING + BLACK_BORDER_SIZE, offset_y)

        # Draw the player's guess
        if player_guess is not None:
            x, y = player_guess
            if (opponent_ship_position[0] <= x < opponent_ship_position[0] + ship_length and
                    opponent_ship_position[1] <= y < opponent_ship_position[1] + ship_length):
                # The player hit the opponent's ship
                pygame.draw.rect(screen, YELLOW, (offset_x + GRID_WIDTH + 2 * RED_BORDER_SIZE + 2 * GRID_SPACING +
                                                  BLACK_BORDER_SIZE + y * CELL_SIZE + BLACK_BORDER_SIZE * (y + 1),
                                                  offset_y + RED_BORDER_SIZE + x * CELL_SIZE + RED_BORDER_SIZE * (x + 1),
                                                  CELL_SIZE, CELL_SIZE))
            else:
                # The player missed the opponent's ship
                pygame.draw.rect(screen, WHITE, (offset_x + GRID_WIDTH + 2 * RED_BORDER_SIZE + 2 * GRID_SPACING +
                                                 BLACK_BORDER_SIZE + y * CELL_SIZE + BLACK_BORDER_SIZE * (y + 1),
                                                 offset_y + RED_BORDER_SIZE + x * CELL_SIZE + RED_BORDER_SIZE * (x + 1),
                                                 CELL_SIZE, CELL_SIZE))



    # Draw the red button with text "Rotate"
##    rotate_button_rect = pygame.Rect((screen_width - 200) // 2 + 250, screen_height - 240, 100, 50)
##    pygame.draw.rect(screen, RED, rotate_button_rect)
##    rotate_button_text = font.render("Rotate", True, BLACK)
##    rotate_button_text_rect = rotate_button_text.get_rect(center=rotate_button_rect.center)
##    screen.blit(rotate_button_text, rotate_button_text_rect)

    pygame.draw.rect(screen, rotate_button_color, rotate_button_rect)
    button_text = font.render("Rotate", True, (255, 255, 255))
    screen.blit(button_text, (rotate_button_rect.centerx - button_text.get_width() // 2,
                              rotate_button_rect.centery - button_text.get_height() // 2))

    # Draw the red button with text "Start"
    start_button_rect = pygame.Rect((screen_width - 200) // 2  + 250, screen_height - 300, 100, 50)
    pygame.draw.rect(screen, RED, start_button_rect)
    start_button_text = font.render("Start", True, BLACK)
    start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)
    screen.blit(start_button_text, start_button_text_rect)

    running = None

    if event.type == pygame.MOUSEBUTTONDOWN and start_button_rect.collidepoint(mouse_x, mouse_y) and event.button == 1:
        running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                col = mouseX // CELL_SIZE
                row = mouseY // CELL_SIZE

            # Check if the mouse click is within the grid bounds
                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
                    # target_row = row
                    # target_col = col
                    print(f"Selected square at row {row + 1}, col {col + 1}")
                    # grid[row][col] = 1  # You can update the grid state here

                    target_square(row, col)






##    if show_rotate_button:
##        # Draw the red button with text "Rotate"
##        button_rect = pygame.Rect((screen_width - 200) // 2  + 250, screen_height - 240, 100, 50)
##        pygame.draw.rect(screen, RED, button_rect)
##        button_text = font.render("Rotate", True, BLACK)
##        button_text_rect = button_text.get_rect(center=button_rect.center)
##        screen.blit(button_text, button_text_rect)
##
##    if show_start_button:
##        # Draw the red button with text "Start"
##        start_button_rect = pygame.Rect((screen_width - 200) // 2  + 250, screen_height - 300, 100, 50)
##        pygame.draw.rect(screen, RED, start_button_rect)
##        start_button_text = font.render("Start", True, BLACK)
##        start_button_text_rect = start_button_text.get_rect(center=start_button_rect.center)
##        screen.blit(start_button_text, start_button_text_rect)

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(60)
