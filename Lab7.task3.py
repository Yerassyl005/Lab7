import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка параметров окна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Радиус и начальные координаты шара
radius = 25
x = WIDTH // 2
y = HEIGHT // 2

# Основной цикл программы
while True:
    screen.fill((255, 255, 255))  # Заливка экрана белым цветом

    # Рисование шара
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Перемещение шара в зависимости от нажатой клавиши
            if event.key == pygame.K_UP:
                if y - 20 >= radius:  # Проверка, чтобы шар не вышел за верхнюю границу экрана
                    y -= 20
            elif event.key == pygame.K_DOWN:
                if y + 20 <= HEIGHT - radius:  # Проверка, чтобы шар не вышел за нижнюю границу экрана
                    y += 20
            elif event.key == pygame.K_LEFT:
                if x - 20 >= radius:  # Проверка, чтобы шар не вышел за левую границу экрана
                    x -= 20
            elif event.key == pygame.K_RIGHT:
                if x + 20 <= WIDTH - radius:  # Проверка, чтобы шар не вышел за правую границу экрана
                    x += 20

    pygame.display.flip()  # Обновление экрана
