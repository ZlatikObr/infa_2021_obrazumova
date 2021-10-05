import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 1000))
clock = pygame.time.Clock()
finished = False


def back():
    rect(screen, (128, 128, 128), (0, 350, 1000, 700), 10000)
    rect(screen, (255, 255, 255), (0, 350, 700, 700))
    rect(screen, (255, 255, 255), (0, 550, 1000, 500))
    


def iglu(x,y):
    circle(screen, (192, 192, 192), (x+185, y+550), 175)
    circle(screen, (0, 0, 0), (x+185, y+550), 175, 3)
    rect(screen, (192, 192, 192), (x+0, y+570, 1000, 500))

    aaline(screen, (0, 0, 0), (x+10, y+570), (x+30, y+573))
    aaline(screen, (0, 0, 0), (x+30, y+573), (x+350, y+573))
    aaline(screen, (0, 0, 0), (x+350, y+573), (x+360, y+571))

    aaline(screen, (0, 0, 0), (x+30, y+490), (x+40, y+490))
    aaline(screen, (0, 0, 0), (x+40, y+490), (x+100, y+498))
    aaline(screen, (0, 0, 0), (x+100, y+498), (x+280, y+498))
    aaline(screen, (0, 0, 0), (x+280, y+498), (x+348, y+490))


    aaline(screen, (0, 0, 0), (x+50, y+440), (x+100, y+450))
    aaline(screen, (0, 0, 0), (x+100, y+450), (x+290, y+450))
    aaline(screen, (0, 0, 0), (x+290, y+450), (x+320, y+440))

    aaline(screen, (0, 0, 0), (x+91, y+400), (x+245, y+400))
    aaline(screen, (0, 0, 0), (x+245, y+400), (x+265, y+395))


    aaline(screen, (0, 0, 0), (x+20, y+570), (x+21, y+490))
    aaline(screen, (0, 0, 0), (x+120, y+570), (x+111, y+500))
    aaline(screen, (0, 0, 0), (x+225, y+570), (x+206, y+500))
    aaline(screen, (0, 0, 0), (x+290, y+570), (x+288, y+500))
    aaline(screen, (0, 0, 0), (x+340, y+570), (x+338, y+490))


    aaline(screen, (0, 0, 0), (x+50, y+490), (x+55, y+440))
    aaline(screen, (0, 0, 0), (x+140, y+498), (x+139, y+448))
    aaline(screen, (0, 0, 0), (x+200, y+498), (x+200, y+448))
    aaline(screen, (0, 0, 0), (x+300, y+498), (x+308, y+440))

    aaline(screen, (0, 0, 0), (x+127, y+450), (x+130, y+400))
    aaline(screen, (0, 0, 0), (x+240, y+450), (x+240, y+400))

    aaline(screen, (0, 0, 0), (x+180, y+400), (x+200, y+380))


def cat(x, y):
    ellipse(screen, (242, 243, 244), (x+100, y+680, 150, 40))
    circle(screen, (242, 243, 244), (x+130, y+665), 30)

    polygon(screen, (242, 243, 244), [[x+110, y+640], [x+118, y+620], [x+121, y+635]])
    polygon(screen, (242, 243, 244), [[x+137, y+640], [x+140, y+620], [x+148, y+635]])

    circle(screen, (255, 255, 255), (x+121, y+655), 10)
    circle(screen, (255, 255, 255), (x+137, y+655), 10)

    circle(screen, (0, 0, 0), (x+120, y+655), 5)
    circle(screen, (0, 0, 0), (x+136, y+655), 5)
    aaline(screen, (0, 0, 0), (x+120, y+670), (x+126, y+670), 5)


    ellipse(screen, (242, 243, 244), (x+120, y+714, 40, 20), 100)
    ellipse(screen, (242, 243, 244), (x+200, y+714, 40, 20), 100)




def escimos(x, y):
    circle(screen, (222, 223, 224), (x+450, y+490), 70)
    ellipse(screen, (101, 67, 33), (x+405, y+495, 100, 200), 100)
    rect(screen, (116, 78, 59), (x+440, y+520, 30, 100))
    rect(screen, (116, 78, 59), (x+406.5, y+590, 100, 30))
    circle(screen, (101,67,33), (x+450, y+490), 50)
    circle(screen, (242, 243, 244), (x+450, y+490), 35)

    rect(screen, (192, 192, 192), (x+405, y+620, 100, 100))

    ellipse(screen, (101, 67, 33), (x+420, y+610, 20, 30), 100)
    ellipse(screen, (101, 67, 33), (x+460, y+610, 20, 30), 100)
    rect(screen, (116, 78, 59), (x+406.5, y+590, 100, 30))

    ellipse(screen, (101, 67, 33), (x+410, y+630, 40, 15), 100)
    ellipse(screen, (101, 67, 33), (x+460, y+630, 40, 15), 100)

    ellipse(screen, (101, 67, 33), (x+410, y+580, 40, 20), 100)
    ellipse(screen, (101, 67, 33), (x+460, y+580, 40, 20), 100)

    aaline(screen, (0, 0, 0), (x+460, y+660), (x+420, y+500))

    aaline(screen, (0, 0, 0), (x+430, y+470), (x+440, y+475), 3)
    aaline(screen, (0, 0, 0), (x+460, y+475), (x+470, y+470), 3)

    aaline(screen, (0, 0, 0), (x+435, y+500), (x+465, y+500))




back()
iglu(100,-150)
iglu(0, -100)
iglu(0,0)
escimos(0,0)
escimos (-100,0)
escimos (-200,20)
escimos (100, 100)
cat(0, -100)
cat(100,0)
cat(200, 200)
cat(0,0)
pygame.display.update()
i=0


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
