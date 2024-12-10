import pygame
from CONST import *


class ChessPiece:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.image = None

    def draw(self, screen):
        if self.image:
            rect = self.image.get_rect(center=(self.x * CELL_SIZE+FRAME_SIZE + CELL_SIZE // 2,
                                               self.y * CELL_SIZE+FRAME_SIZE + CELL_SIZE // 2))
            screen.blit(self.image, rect)

    def get_possible_moves(self, board):
        return []


class King(ChessPiece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = pygame.image.load(f"img/{color}K.png").convert_alpha()

    def get_possible_moves(self, board):
        moves = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < 8 and 0 <= ny < 8 and not board.is_occupied(nx, ny, self.color):
                    moves.append((nx, ny))
        return moves


class Knight(ChessPiece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = pygame.image.load(f"img/{color}N.png").convert_alpha()

    def get_possible_moves(self, board):
        moves = []
        for dx, dy in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and not board.is_occupied(nx, ny, self.color):
                moves.append((nx, ny))
        return moves


class Queen(ChessPiece):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.image = pygame.image.load(f"img/{color}Q.png").convert_alpha()

    def get_possible_moves(self, board):
        moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        for dx, dy in directions:
            nx, ny = self.x, self.y
            while True:
                nx, ny = nx + dx, ny + dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if board.is_occupied(nx, ny, self.color):
                        break
                    moves.append((nx, ny))
                    if board.is_occupied(nx, ny):
                        break
                else:
                    break
        return moves
