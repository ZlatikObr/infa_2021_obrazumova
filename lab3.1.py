import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 1000))

rect(screen, (128, 128, 128), (0, 350, 1000, 700), 10000)
rect(screen, (255, 255, 255), (0, 350, 700, 700))
rect(screen, (255, 255, 255), (0, 550, 1000, 500))
circle(screen, (192, 192, 192), (185, 550), 175)
circle(screen, (0, 0, 0), (185, 550), 175, 3)
rect(screen, (192, 192, 192), (0, 570, 1000, 500))

aaline(screen, (0, 0, 0), (10, 570), (30, 573))
aaline(screen, (0, 0, 0), (30, 573), (350, 573))
aaline(screen, (0, 0, 0), (350, 573), (360, 571))

aaline(screen, (0, 0, 0), (30, 490), (40, 490))
aaline(screen, (0, 0, 0), (40, 490), (100, 498))
aaline(screen, (0, 0, 0), (100, 498), (280, 498))
aaline(screen, (0, 0, 0), (280, 498), (348, 490))


aaline(screen, (0, 0, 0), (50, 440), (100, 450))
aaline(screen, (0, 0, 0), (100, 450), (290, 450))
aaline(screen, (0, 0, 0), (290, 450), (320, 440))

aaline(screen, (0, 0, 0), (91, 400), (245, 400))
aaline(screen, (0, 0, 0), (245, 400), (265, 395))


aaline(screen, (0, 0, 0), (20, 570), (21, 490))
aaline(screen, (0, 0, 0), (120, 570), (111, 500))
aaline(screen, (0, 0, 0), (225, 570), (206, 500))
aaline(screen, (0, 0, 0), (290, 570), (288, 500))
aaline(screen, (0, 0, 0), (340, 570), (338, 490))


aaline(screen, (0, 0, 0), (50, 490), (55, 440))
aaline(screen, (0, 0, 0), (140, 498), (139, 448))
aaline(screen, (0, 0, 0), (200, 498), (200, 448))
aaline(screen, (0, 0, 0), (300, 498), (308, 440))

aaline(screen, (0, 0, 0), (127, 450), (130, 400))
aaline(screen, (0, 0, 0), (240, 450), (240, 400))

aaline(screen, (0, 0, 0), (180, 400), (200, 380))

circle(screen, (242, 243, 244), (550, 490), 70)
ellipse(screen, (101, 67, 33), (505, 495, 100, 200), 100)
rect(screen, (116, 78, 59), (540, 520, 30, 100))
rect(screen, (116, 78, 59), (506.5, 590, 100, 30))
circle(screen, (101,67,33), (550, 490), 50)
circle(screen, (242, 243, 244), (550, 490), 35)

rect(screen, (192, 192, 192), (0, 620, 1000, 500))

ellipse(screen, (101, 67, 33), (520, 610, 20, 30), 100)
ellipse(screen, (101, 67, 33), (560, 610, 20, 30), 100)
rect(screen, (116, 78, 59), (506.5, 590, 100, 30))

ellipse(screen, (101, 67, 33), (510, 630, 40, 15), 100)
ellipse(screen, (101, 67, 33), (560, 630, 40, 15), 100)

ellipse(screen, (101, 67, 33), (510, 580, 40, 20), 100)
ellipse(screen, (101, 67, 33), (560, 580, 40, 20), 100)

aaline(screen, (0, 0, 0), (560, 660), (520, 500))

aaline(screen, (0, 0, 0), (530, 470), (540, 475), 3)
aaline(screen, (0, 0, 0), (560, 475), (570, 470), 3)

aaline(screen, (0, 0, 0), (535, 500), (565, 500))

ellipse(screen, (242, 243, 244), (100, 680, 150, 40))
circle(screen, (242, 243, 244), (130, 665), 30)

polygon(screen, (242, 243, 244), [[110, 640], [118, 620], [121, 635]])
polygon(screen, (242, 243, 244), [[137, 640], [140, 620], [148, 635]])

circle(screen, (255, 255, 255), (121, 655), 10)
circle(screen, (255, 255, 255), (137, 655), 10)

circle(screen, (0, 0, 0), (120, 655), 5)
circle(screen, (0, 0, 0), (136, 655), 5)
aaline(screen, (0, 0, 0), (120, 670), (126, 670), 5)


ellipse(screen, (242, 243, 244), (120, 714, 40, 20), 100)
ellipse(screen, (242, 243, 244), (200, 714, 40, 20), 100)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
