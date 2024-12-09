import pygame

from Login import Class_Login

# Параметры окна

WIDTH_BOAR, HEIGHT_BOARD = 500, 500

# Инициализация Pygame
pygame.init()


def main():
    while True:
        login = Class_Login()
        login.start_login()

        if login:
            pass 
        break


pygame.quit()


if __name__ == "__main__":
    main()

