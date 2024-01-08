import random
import pygame
pygame.init()
def duongbao(a,b,c,d):
    pygame.draw.line(screen, black, a, b, 5)
    pygame.draw.line(screen, black, b, c, 5)
    pygame.draw.line(screen, black, c, d, 5)
    pygame.draw.line(screen, black, d, a, 5)
def xoayxx():
    return [random.randint(1,6), random.randint(1,6), random.randint(1,6)]
def vexucsac(lst):
    pygame.draw.circle(screen, white, (500, 150), (150))
    pygame.draw.circle(screen, black, (500, 150), (150),5)
    if lst[0] == 1:
        pygame.draw.rect(screen, grey, (475, 55, 50, 50))
        pygame.draw.circle(screen, black, (500, 80), (5))
    elif lst[0] == 2:
        pygame.draw.rect(screen, grey, (475, 55, 50, 50))
        pygame.draw.circle(screen, black, (490, 80), (5))
        pygame.draw.circle(screen, black, (510, 80), (5))
    elif lst[0] == 3:
        pygame.draw.rect(screen, grey, (475, 55, 50, 50))
        pygame.draw.circle(screen, black, (500, 70), (5))
        pygame.draw.circle(screen, black, (490, 85), (5))
        pygame.draw.circle(screen, black, (510, 85), (5))
    elif lst[0] == 4:
        pygame.draw.rect(screen, grey, (475, 55, 50, 50))
        pygame.draw.circle(screen, black, (490, 70), (5))
        pygame.draw.circle(screen, black, (490, 90), (5))
        pygame.draw.circle(screen, black, (510, 70), (5))
        pygame.draw.circle(screen, black, (510, 90), (5))
    elif lst[0] == 5:
        pygame.draw.rect(screen, grey, (475, 55, 50, 50))
        pygame.draw.circle(screen, black, (490, 70), (5))
        pygame.draw.circle(screen, black, (490, 90), (5))
        pygame.draw.circle(screen, black, (510, 70), (5))
        pygame.draw.circle(screen, black, (510, 90), (5))
        pygame.draw.circle(screen, black, (500, 80), (5))
    elif lst[0] == 6:
        pygame.draw.rect(screen, grey, (475, 55, 50, 50))
        pygame.draw.circle(screen, black, (490, 65), (5))
        pygame.draw.circle(screen, black, (490, 80), (5))
        pygame.draw.circle(screen, black, (490, 95), (5))
        pygame.draw.circle(screen, black, (510, 65), (5))
        pygame.draw.circle(screen, black, (510, 80), (5))
        pygame.draw.circle(screen, black, (510, 95), (5))
    if lst[1] == 1:      
        pygame.draw.rect(screen, grey, (425, 170, 50, 50))
        pygame.draw.circle(screen, black, (450, 195), (5))
    elif lst[1] == 2:
        pygame.draw.rect(screen, grey, (425, 170, 50, 50))
        pygame.draw.circle(screen, black, (440, 195), (5))
        pygame.draw.circle(screen, black, (460, 195), (5))
    elif lst[1] == 3:
        pygame.draw.rect(screen, grey, (425, 170, 50, 50))
        pygame.draw.circle(screen, black, (450, 185), (5))
        pygame.draw.circle(screen, black, (440, 200), (5))
        pygame.draw.circle(screen, black, (460, 200), (5))
    elif lst[1] == 4:
        pygame.draw.rect(screen, grey, (425, 170, 50, 50))
        pygame.draw.circle(screen, black, (440, 185), (5))
        pygame.draw.circle(screen, black, (440, 205), (5))
        pygame.draw.circle(screen, black, (460, 205), (5))
        pygame.draw.circle(screen, black, (460, 185), (5))
    elif lst[1] == 5:
        pygame.draw.rect(screen, grey, (425, 170, 50, 50))
        pygame.draw.circle(screen, black, (440, 185), (5))
        pygame.draw.circle(screen, black, (440, 205), (5))
        pygame.draw.circle(screen, black, (460, 205), (5))
        pygame.draw.circle(screen, black, (460, 185), (5))
        pygame.draw.circle(screen, black, (450, 195), (5))
    elif lst[1] == 6:
        pygame.draw.rect(screen, grey, (425, 170, 50, 50))
        pygame.draw.circle(screen, black, (440, 180), (5))
        pygame.draw.circle(screen, black, (440, 195), (5))
        pygame.draw.circle(screen, black, (440, 210), (5))
        pygame.draw.circle(screen, black, (460, 180), (5))
        pygame.draw.circle(screen, black, (460, 195), (5))
        pygame.draw.circle(screen, black, (460, 210), (5))
    if lst[2] == 1:       
        pygame.draw.rect(screen, grey, (525, 170, 50, 50))
        pygame.draw.circle(screen, black, (550, 195), (5))
    elif lst[2] == 2:
        pygame.draw.rect(screen, grey, (525, 170, 50, 50))
        pygame.draw.circle(screen, black, (540, 195), (5))
        pygame.draw.circle(screen, black, (560, 195), (5))
    elif lst[2] == 3:
        pygame.draw.rect(screen, grey, (525, 170, 50, 50))
        pygame.draw.circle(screen, black, (550, 185), (5))
        pygame.draw.circle(screen, black, (540, 200), (5))
        pygame.draw.circle(screen, black, (560 ,200), (5))
    elif lst[2] == 4:
        pygame.draw.rect(screen, grey, (525, 170, 50, 50))
        pygame.draw.circle(screen, black, (540, 205), (5))
        pygame.draw.circle(screen, black, (540, 185), (5))
        pygame.draw.circle(screen, black, (560, 205), (5))
        pygame.draw.circle(screen, black, (560, 185), (5))
    elif lst[2] == 5:
        pygame.draw.rect(screen, grey, (525, 170, 50, 50))
        pygame.draw.circle(screen, black, (540, 205), (5))
        pygame.draw.circle(screen, black, (540, 185), (5))
        pygame.draw.circle(screen, black, (560, 205), (5))
        pygame.draw.circle(screen, black, (560, 185), (5))
        pygame.draw.circle(screen, black, (550, 195), (5))
    elif lst[2] == 6:
        pygame.draw.rect(screen, grey, (525, 170, 50, 50))
        pygame.draw.circle(screen, black, (540, 180), (5))
        pygame.draw.circle(screen, black, (540, 195), (5))
        pygame.draw.circle(screen, black, (540, 210), (5))
        pygame.draw.circle(screen, black, (560, 180), (5))
        pygame.draw.circle(screen, black, (560, 195), (5))
        pygame.draw.circle(screen, black, (560, 210), (5))
def taixiubutton():
    at,bt,ct,dt = (100,500),(300,500),(300,700),(100,700)
    duongbao(at,bt,ct,dt)
    ax,bx,cx,dx = (700,500),(900,500),(900,700),(700,700)
    duongbao(ax,bx,cx,dx)
    pygame.draw.rect(screen, white, (100, 500, 200, 200))
    pygame.draw.rect(screen, white, (700, 500, 200, 200))
    pygame.draw.circle(screen, grey, (500, 150), (150))
    pygame.draw.circle(screen, black, (500, 150), (150),5)
    a = font.render('Tai', True, black)
    b = a.get_rect(center = (200, 600))
    c = font.render('Xiu', True, black)
    d = c.get_rect(center = (800, 600))
    screen.blit(a,b)
    screen.blit(c,d)
def choibutton():
    a,b,c,d = (300,300),(700,300),(700,500),(300,500)
    duongbao(a,b,c,d)
    pygame.draw.rect(screen, white, (300, 300, 400, 200))
    a = font.render('Get started!', True, red)
    b = a.get_rect(center = (500, 400))
    screen.blit(a,b)
def winorlose(player):
    pygame.draw.rect(screen, white, (300, 300, 400, 200))
    if player:
        a = font.render('You Win!', True, black)
        b = a.get_rect(center = (500, 400))
        screen.blit(a,b)
    else:
        a = font.render('You Lose!', True, black)
        b = a.get_rect(center = (500, 400))
        screen.blit(a,b)
def playagain():
    pygame.draw.rect(screen, white, (300, 500, 400, 200))
    pygame.draw.line(screen, black, (300, 500), (700, 500), 3)
    a = font.render('Play Again', True, black)
    b = a.get_rect(center = (500, 600))
    screen.blit(a, b)
    a1,b1,c1,d1 = (300,300),(700,300),(700,700),(300,700)
    duongbao(a1,b1,c1,d1)
red = (178,34,34)
white = (255, 255, 255)
grey = (194, 194, 214)
black = (64, 64, 64)
font = pygame.font.Font('04B_19__.TTF', 60)
screen = pygame.display.set_mode((1000, 800))
run = True
choibutton_ = True
vexucsac_ = False
taixiubutton_ = False
winorlose_ = False
playeragain_ = False
while run:
    screen.fill(red)
    if choibutton_: choibutton()
    if vexucsac_ : vexucsac(lst)
    if taixiubutton_: taixiubutton()
    if winorlose_: winorlose(player)
    if playeragain_: playagain()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            toa_do = list(event.pos)
            x = toa_do[0]
            y = toa_do[1]
            if choibutton_:
                if event.button == 1 and (x>=300 and x<=700) and (y>=300 and y<=500):
                    choibutton_ = False
                    taixiubutton_ = True
            if taixiubutton_:             
                if event.button == 1 and (x>=700 and x<=900) and(y>=500 and y<=700):
                    taixiubutton_ = False
                    vexucsac_ = True
                    lst = xoayxx()
                    player = 'xiu'
                    winorlose_ = True
                    if sum(lst) >= 11:
                        player = False
                    else:
                        player = True
                    playeragain_ = True
                if event.button == 1 and (x>=100 and x<=300) and(y>=500 and y<=700):
                    taixiubutton_ = False
                    vexucsac_ = True
                    lst = xoayxx()
                    player = 'tai'
                    winorlose_ = True
                    if sum(lst) >= 11:
                        player = True
                    else:
                        player = False
                    playeragain_ = True
            if playeragain_:
                if event.button == 1 and (x>=300 and x<=700) and(y>=500 and y<=700):
                    taixiubutton_ = True
                    winorlose_ = False
                    playeragain_ = False                            
    pygame.display.flip()
pygame.quit()