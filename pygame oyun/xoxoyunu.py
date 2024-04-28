import pygame
import sys

# Oyun ekranı boyutları
WIDTH, HEIGHT = 300, 300
# Oyun tahtası boyutları
BOARD_SIZE = 3
# Kare boyutu
SQUARE_SIZE = WIDTH // BOARD_SIZE

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)

# Oyun tahtası oluşturma
def create_board():
    return [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Tahta çizimi
def draw_board(screen, board):
    screen.fill(WHITE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)
            font = pygame.font.SysFont(None, 80)
            text = font.render(board[row][col], True, BLACK)
            text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
            screen.blit(text, text_rect)

# Oyun tahtasında boş kareleri kontrol etme
def is_board_full(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == " ":
                return False
    return True

# Kazananı kontrol etme
def check_winner(board):
    # Rows and Columns
    for i in range(BOARD_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("XOX Game")
    clock = pygame.time.Clock()

    board = create_board()
    turn = "X"
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // SQUARE_SIZE
                row = y // SQUARE_SIZE

                if board[row][col] == " ":
                    board[row][col] = turn
                    winner = check_winner(board)
                    if winner:
                        game_over = True
                    elif is_board_full(board):
                        game_over = True
                    turn = "O" if turn == "X" else "X"

        draw_board(screen, board)

        if game_over:
            font = pygame.font.SysFont(None, 50)
            if winner:
                text = font.render(f"Oyuncu {winner} Kazandı!", True, RED)
            else:
                text = font.render("berabere!", True, GREEN)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
