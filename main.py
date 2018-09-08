from random import randint

import pygame

FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DISPLAY = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def get_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


class Square:
    width = 50
    height = 50

    def __init__(self, x, y, speed_x, speed_y):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = WHITE

    def calculate_next_position(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x + self.width >= WIN_WIDTH:
            self.speed_x = -self.speed_x
            self.color = get_random_color()

        if self.y <= 0 or self.y + self.height >= WIN_HEIGHT:
            self.speed_y = -self.speed_y
            self.color = get_random_color()

    def draw(self):
        pygame.draw.rect(DISPLAY, self.color, (self.x, self.y, self.width, self.height))


def main():
    pygame.init()
    clock = pygame.time.Clock()

    pygame.display.update()

    square = Square(0, 0, 4, 5)

    while 1:

        DISPLAY.fill(BLACK)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

        square.draw()

        pygame.display.update()
        square.calculate_next_position()

        clock.tick(FPS)


if __name__ == '__main__':
    main()
