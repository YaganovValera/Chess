import pygame

import Class_Board
import Class_Piece
import Class_Setting
from CONST import *
# Параметры доски


class ClassGameChess:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
        self.clock = pygame.time.Clock()
        self.running = True
        self.quit_game = False
        pygame.display.set_caption("Эндшпиль: Король, 2 коня - Король, ферзь")
        self.board = Class_Board.ChessBoard(self.screen)
        self.settings = Class_Setting.ClassSetting(self.screen, WIDTH_BOARD, FRAME_SIZE)
        self.setup_pieces()

    def setup_pieces(self):
        # Установка фигур на доске
        self.board.add_piece(Class_Piece.King(4, 7, COLOR_W))
        self.board.add_piece(Class_Piece.Knight(3, 7, COLOR_W))
        self.board.add_piece(Class_Piece.Knight(5, 7, COLOR_W))
        self.board.add_piece(Class_Piece.Queen(3, 0, COLOR_B))
        self.board.add_piece(Class_Piece.King(4, 0, COLOR_B))

    def run(self):
        while not self.quit_game:
            self.handle_events()
            self.render()
            self.clock.tick(30)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.quit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                button_action = self.settings.handle_click(event.pos)
                if button_action == "Сменить сторону":
                    self.board.color_player = COLOR_B if self.board.color_player == COLOR_W else COLOR_W


    def render(self):
        self.screen.fill(WHITE)
        self.board.draw_board()
        self.settings.draw(None)
        for row in self.board.board:
            for piece in row:
                if piece:
                    piece.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = ClassGameChess()
    game.run()
