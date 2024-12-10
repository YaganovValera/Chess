import pygame
from CONST import *


class ChessBoard:
    def __init__(self, screen):
        self.screen = screen
        self.color_player = COLOR_W         # c чьей стороны будет отрисовка
        self.color_cur_move = True          # чей ход True - белых, False - черных
        self.selected_piece = None          # выбранная фигура
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def add_piece(self, piece):
        self.board[piece.y][piece.x] = piece

    def move_piece(self, piece, x, y):
        self.board[piece.y][piece.x] = None
        piece.x, piece.y = x, y
        self.board[y][x] = piece

    def clear_board(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.color_player = COLOR_W

    def handle_click_game_start(self, mouse_pos):
        pass

    def handle_click_game_stop(self, mouse_pos):
        # Определяем размер клетки
        x, y = (mouse_pos[0] - FRAME_SIZE) // CELL_SIZE, (mouse_pos[1] - FRAME_SIZE) // CELL_SIZE
        # Проверяем, что клик внутри доски
        if 0 <= x < 8 and 0 <= y < 8:
            selected_piece = self.board[y][x]
            if selected_piece:                              # Если кликнули на фигуру
                self.selected_piece = (selected_piece, x, y)
            elif self.selected_piece is not None:           # Если фигура уже выбрана, пытаемся ее переместить
                piece, old_x, old_y = self.selected_piece
                # Перемещаем фигуру
                self.board[old_y][old_x] = None
                self.board[y][x] = piece
                piece.x, piece.y = x, y
                self.selected_piece = None

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

        # отрисовка выбранной фигуры
        if self.selected_piece:
            _, old_x, old_y = self.selected_piece
            pygame.draw.rect(
                self.screen, RED,
                (old_x * CELL_SIZE + FRAME_SIZE, old_y * CELL_SIZE + FRAME_SIZE, CELL_SIZE, CELL_SIZE), 3
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

    def is_occupied(self, x, y, color=None):
        """
        Проверяет, занята ли клетка на доске.
        :param x: Координата x клетки.
        :param y: Координата y клетки.
        :param color: Цвет фигуры, с которым нужно сравнить (если указано).
        :return:
            True, если клетка занята и цвет совпадает (или любой, если color=None).
            False, если клетка пуста или цвет не совпадает.
        """
        piece = self.board[y][x]  # Получаем фигуру на указанной клетке
        if piece is None:  # Если клетка пуста
            return False
        if color is None:  # Если цвет не указан, клетка считается занятой
            return True
        return piece.color == color  # Сравниваем цвет фигуры на клетке с заданным

