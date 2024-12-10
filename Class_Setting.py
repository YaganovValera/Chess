import pygame
from CONST import *


class ClassSetting:
    def __init__(self, screen, board_width, frame_size):
        self.screen = screen
        self.start_x = board_width + frame_size*2 + 20
        self.frame_size = frame_size
        self.panel_width = 200
        self.buttons = []
        self.init_buttons()

    def init_buttons(self):
        # Настройка кнопок
        button_width, button_height = 150, 40
        start_x = self.start_x
        start_y = self.frame_size + 70

        self.buttons = [
            {"label": "Сменить сторону", "rect": pygame.Rect(start_x, start_y, button_width, button_height)},
            {"label": "Начать играть", "rect": pygame.Rect(start_x, start_y + 60, button_width, button_height)},
            {"label": "Начать заново", "rect": pygame.Rect(start_x, start_y + 120, button_width, button_height)},
        ]

    def draw(self, winner=None):
        if winner is None:
            result = "-"
        else:
            result = "Б" if winner else "Ч"
        # Отображение победителя
        font = pygame.font.SysFont("TimesNewRoman", 28)
        text_winner = font.render(f"Победитель: {result}", True, BLACK)
        self.screen.blit(text_winner, (self.start_x, self.frame_size + 20))

        font_button = pygame.font.SysFont("TimesNewRoman", 14)
        # Отрисовка кнопок
        for button in self.buttons:
            pygame.draw.rect(self.screen, WHITE, button["rect"])
            pygame.draw.rect(self.screen, BLACK, button["rect"], 2)
            label = font_button.render(button["label"], True, BLACK)
            label_rect = label.get_rect(center=button["rect"].center)
            self.screen.blit(label, label_rect)

    def handle_click(self, mouse_pos):
        for button in self.buttons:
            if button["rect"].collidepoint(mouse_pos):
                return button["label"]
        return None
