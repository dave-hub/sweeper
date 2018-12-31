import pygame
import random
import sys
from pygame.locals import *

pygame.init()

size = 600, 900
bgcolor = 0, 0, 0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class dot:
    def __init__(self):
        self.start = random.randint(0, 585), random.randint(450, 885)
        self.dot = pygame.Surface((15, 15))
        self.rect = self.dot.get_rect()
        self.color = 0, 0, 0
        self.scramble((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        self.selected = False
        self.selectIndicator = pygame.Surface((21, 21))
        self.selectIndicatorRect = self.selectIndicator.get_rect()
        self.check = True

    def collisioncheck(self):
        for i in range(0, len(blocktest.barsrect)):
            if blocktest.barsrect[i].colliderect(self.rect):
                self.rect.top = -600
                self.rect.left = -600
                self.check = False
                return True
        return False

    def draw(self):
        if self.selected:
            self.selectIndicator.fill((0,0,0))
            self.selectIndicatorRect.top, self.selectIndicatorRect.left = self.rect.top - 3, self.rect.left - 3
            screen.blit(self.selectIndicator, self.selectIndicatorRect)
        self.dot.fill(self.color)
        screen.blit(self.dot, self.rect)

    def scramble(self, color):
        self.rect.top = random.randint(450, 885)
        self.rect.left = random.randint(0, 585)
        self.color = color
        self.check = True


class block:
    def __init__(self):
        self.holes = random.randint(3, 8)
        self.bars = []
        self.barsrect = []
        self.counter = 0
        self.gotime = 0
        self.moving = False
        self.wins = 5
        for i in range(0, 20):
            self.bars.append(pygame.Surface((30,30)))
            self.barsrect.append(self.bars[i].get_rect())
            self.barsrect[i].top, self.barsrect[i].left = -40, 30 * i

    def scramble(self, color):
        self.holes = random.randint(3, 8)
        self.bars = []
        self.barsrect = []
        self.hintspos = []
        self.counter = 0
        self.gotime = random.randint(300, 700)
        self.moving = False
        self.hintcut = random.randint(0, 3)
        for i in range(0, 20):
            self.bars.append(pygame.Surface((30,30)))
            self.barsrect.append(self.bars[i].get_rect())
            self.barsrect[i].top, self.barsrect[i].left = -40, 30 * i
        for i in range(0, self.holes):
            ind = random.randint(0, len(self.bars)-1)
            num = (self.barsrect[ind].left - 15) + random.randint(-100, 100)
            self.hintspos.append(num)
            self.bars.pop(ind)
            self.barsrect.pop(ind)
        for i in range(0, len(self.bars)):
            self.bars[i].fill(color)
        for i in range(0, self.hintcut):
            ind = random.randint(0, len(self.hintspos)-1)
            self.hintspos.pop(ind)


    def move(self):
        if self.counter == self.gotime:
            self.moving = True
            for i in range(0, len(self.barsrect)):
                self.barsrect[i].top += 8
        else:
            self.counter += 1

    def draw(self):
        for i in range(0, len(self.bars)):
            screen.blit(self.bars[i], self.barsrect[i])


def scramble(dotcount):
    global bgcolor, dotsList
    color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    bgcolor = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    dotsList = []
    blocktest.wins = dotcount
    for i in range(0, dotcount):
        dotsList.append(dot())
        dotsList[i].scramble(color)
    blocktest.scramble(color)


def drawhints(col):
    for i in range(len(blocktest.hintspos)):
        a = blocktest.hintspos[i] - 15, 0
        b = blocktest.hintspos[i] + 15, 0
        c = blocktest.hintspos[i], 26
        pygame.draw.polygon(screen, col, (a, b, c))



dotsList = []
for i in range(0, 5):
    dotsList.append(dot())


blocktest = block()
blocktest.scramble((0,0,0))


scramble(5)


def MENU():
    menuimg = pygame.image.load("menu.png")
    menu = menuimg.get_rect()

    playbutton = pygame.Rect((51, 319), (505, 216))
    exitbutton = pygame.Rect((520, 0), (80, 43))
    howtbutton = pygame.Rect((0, 847), (210, 53))
    infobutton = pygame.Rect((520, 855), (80, 46))

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if playbutton.collidepoint(x, y):
                    GAME()
                if exitbutton.collidepoint(x, y):
                    sys.exit()
                if howtbutton.collidepoint(x, y):
                    HOWTO()
                if infobutton.collidepoint(x, y):
                    INFO()

        screen.blit(menuimg, menu)
        pygame.display.update()
        clock.tick(30)


def HOWTO():
    howtimg = pygame.image.load("howto.png")
    howt = howtimg.get_rect()

    backbutton = pygame.Rect((500, 0), (100, 45))

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if backbutton.collidepoint(x, y):
                    MENU()

        screen.blit(howtimg, howt)
        pygame.display.update()
        clock.tick(30)


def INFO():
    infoimg = pygame.image.load("info.png")
    info = infoimg.get_rect()

    backbutton = pygame.Rect((500, 0), (100, 45))

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if backbutton.collidepoint(x, y):
                    MENU()

        screen.blit(infoimg, info)
        pygame.display.update()
        clock.tick(30)


def ENDGAME():
    pause = True

    scoreimg = pygame.image.load("scorecard.png")
    scorerect = scoreimg.get_rect()

#   ## draw once, or there's no transparency
    screen.blit(scoreimg, scorerect)

    while pause:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pause = False
            elif event.type == KEYDOWN:
                pause = False

        pygame.display.update()
        clock.tick(30)

    MENU()


def GAME():

    scramble(5)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    scramble(5)
                else:
                    run = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not blocktest.moving:
                        x, y = pygame.mouse.get_pos()
                        if y > 450:
                            cont = True
                            for i in range(0, len(dotsList)):
                                if dotsList[i].selected:
                                    dotsList[i].rect.top, dotsList[i].rect.left = y-7, x-7
                                    dotsList[i].selected = False
                                    cont = False
                                    break

                            if cont:
                                for i in range(0, len(dotsList)):
                                    if dotsList[i].rect.collidepoint(x, y):
                                        dotsList[i].selected = True
                                        break
        blocktest.move()

        if blocktest.barsrect[0].top > 900:
            print "block1", blocktest.wins
            blocktest.wins *= 2
            print "block2", blocktest.wins
            scramble(blocktest.wins)

        for i in range(0, len(dotsList)):
            if dotsList[i].check and dotsList[i].collisioncheck():
                blocktest.wins -= 1
                print "block hit", blocktest.wins

        print "dots", len(dotsList)

        if len(dotsList) == 0:
            print "in here"
            ENDGAME()

        screen.fill(bgcolor)
        for i in range(0, len(dotsList)):
            dotsList[i].draw()
        blocktest.draw()
        drawhints(dotsList[0].color)
        pygame.display.update()
        clock.tick(60)

MENU()