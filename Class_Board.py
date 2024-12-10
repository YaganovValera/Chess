import pygame
from CONST import *


class ChessBoard:
    def __init__(self, screen):
        self.screen = screen
        self.color_player = COLOR_W
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def add_piece(self, piece):
        self.board[piece.y][piece.x] = piece

    def draw_board(self):
        """ Отрисовка шахматной доски """
        # Отрисовка черного фона для краев
        pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH_BOARD + FRAME_SIZE*2, HEIGHT_BOARD + FRAME_SIZE*2))

        # Отрисовка клеток доски
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                color = LIGHT_BROWN if (x + y) % 2 == 0 else DARK_BROWN
                pygame.draw.rect(
                    self.screen, color,
                    (x * CELL_SIZE + FRAME_SIZE, y * CELL_SIZE + FRAME_SIZE, CELL_SIZE, CELL_SIZE)
                )

        # Отрисовка букв внизу (a-h)
        font = pygame.font.SysFont(None, 24)
        letters = "abcdefgh"
        if self.color_player == COLOR_B:
            letters = letters[::-1]
        for i, letter in enumerate(letters):
            text = font.render(letter, True, WHITE)
            text_rect = text.get_rect(
                center=(i * CELL_SIZE + FRAME_SIZE + CELL_SIZE // 2, HEIGHT_WINDOW - FRAME_SIZE // 2))
            self.screen.blit(text, text_rect)

        # Отрисовка цифр слева (1-8 снизу вверх)
        rows = [i for i in range(len(self.board))]
        if self.color_player == COLOR_B:
            rows = rows[::-1]
        for i, letter in enumerate(rows):
            text = font.render(str(8-letter), True, WHITE)
            text_rect = text.get_rect(center=(FRAME_SIZE // 2, i * CELL_SIZE + FRAME_SIZE + CELL_SIZE // 2))
            self.screen.blit(text, text_rect)

    def move_piece(self, piece, x, y):
        self.board[piece.y][piece.x] = None
        piece.x, piece.y = x, y
        self.board[y][x] = piece
