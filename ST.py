import pygame
import random  # Импортируем их

pygame.init()  # Инициализируем pygame

win = pygame.display.set_mode((600, 600))  # Создадим окно 600х600

pygame.display.set_caption("Треугольник Серпинского")

Triangle = [[300, 150], [100, 550], [500, 550]]  # Определим вершины треугольника
x, y = random.randint(0, 600), random.randint(0, 600)  # Определим изначальную точку,
# от которой мы будем рисовать наш треугольник

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    A = random.randint(0, 2)  # Рандомная вершина нашего треугольника
    x, y = .5 * (x + Triangle[A][0]), .5 * (y + Triangle[A][1])  # Вычисляем новую точку
    # треугольника Серпинского по середине между прежней точкой и любой вершиной

    pygame.draw.line(win, (102, 0, 255), (x, y), (x, y), 1)  # Рисуем нашу точку
    pygame.display.update()
pygame.quit()
