from tkinter import *
from random import randrange as rnd, choice
import time
import math


root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red', 'orange', 'yellow', 'blue', 'green']

score = 0


def new_ball():
    #функция отрисовывает шарик
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(10, 30)
    canv.create_oval(x-r, y-r, x+r, y+r,
                     fill=choice(colors), width=0)
    root.after(2000, new_ball)

def new_ball3():
    #функция отрисовывает шарик3
    global z, w, t
    #canv.delete(ALL)
    z = rnd(100, 700)
    w = rnd(100, 500)
    t = rnd(10, 30)
    canv.create_oval(z-t, w-t, z+t, w+t,
                     fill=choice(colors), width=0)
    root.after(2000, new_ball3)


def new_ball2():
    #функция отрисовывает шарик2
    global p, m, n
    #canv.delete(ALL)
    p = rnd(200, 800)
    m = rnd(10, 700)
    n = rnd(20, 40)
    canv.create_oval(p-n, m-n, p+n, m+n,
                     fill=choice(colors), width=0)
    root.after(2000, new_ball2)

def new_bomb():
    #функция отрисовывает квадрат-бомба
    global o, q, e
    #canv.delete(ALL)
    o = rnd(20, 800)
    q = rnd(50, 700)
    e = rnd(20, 40)
    canv.create_rectangle(o, q, o+q, q+o,
                     fill=choice(colors), width=0)
    root.after(2000, new_bomb)

def click(event):
    #добавляет очки при нажатии
    global x, y, r, z, w, t, p, m, n, o, q, e, score
    x1, y1 = event.x, event.y
    if (x1-x)**2 + (y1-y)**2 <= r**2:
        score += 100/r
        print('%.2f' % score)
    z1, w1 = event.x, event.y
    if (z1-z)**2 + (w1-w)**2 <= t**2:
        score += 100/t
        print('%.2f' % score)
    p1, m1 = event.x, event.y
    if (p1-p)**2 + (m1-m)**2 <= n**2:
        score += 100/n
        print('%.2f' % score)
    #снимает очки за нажатие на квадрат
    o1, q1 = event.x, event.y
    if (o1-o)**2 + (q1-q)**2 <= e**2:
        score += 100/e
        print('%.1f' % score)

new_ball()
new_ball2()
new_ball3()
new_bomb()
canv.bind('<Button-1>', click)

root.mainloop()
