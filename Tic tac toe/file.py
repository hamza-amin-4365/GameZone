import pygame
import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
FONT = pygame.font.Font(None, 36)


# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize game variables
board = [["" for _ in range(3)] for _ in range(3)]
player_turn = "X"
game_over = False
winner = None

# Functions
def draw_board():
    for row in range(1, 3):
        pygame.draw.line(SCREEN, LINE_COLOR, (0, row * HEIGHT // 3), (WIDTH, row * HEIGHT // 3), 3)
    for col in range(1, 3):
        pygame.draw.line(SCREEN, LINE_COLOR, (col * WIDTH // 3, 0), (col * WIDTH // 3, HEIGHT), 3)

def draw_text(text, x, y):
    text_surface = FONT.render(text, True, LINE_COLOR)
    SCREEN.blit(text_surface, (x, y))

def check_winner():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if not game_over and event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // (HEIGHT // 3)
            col = x // (WIDTH // 3)
            if board[row][col] == "":
                board[row][col] = player_turn
                player_turn = "O" if player_turn == "X" else "X"
                winner = check_winner()
                if winner or all(board[i][j] != "" for i in range(3) for j in range(3)):
                    game_over = True

    SCREEN.fill(WHITE)
    draw_board()

    for row in range(3):
        for col in range(3):
            cell_value = board[row][col]
            if cell_value != "":
                draw_text(cell_value, col * WIDTH // 3 + 40, row * HEIGHT // 3 + 40)

    if winner:
        draw_text(f"Player {winner} wins!", 80, HEIGHT // 2 - 20)
    elif game_over:
        draw_text("It's a draw!", 120, HEIGHT // 2 - 20)

    pygame.display.update()

pygame.quit()
