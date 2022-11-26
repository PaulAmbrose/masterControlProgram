import pygame
from pygame.locals import *
import sys
import pygwidgets

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

background = pygwidgets.Image(window, (0, 0),
                            'images/tron.png')
newGameButton = pygwidgets.TextButton(window, (20, 530),
                            'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520),
                            'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520),
                            'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530),
                            'Quit', width=100, height=45)

oGame = Game(window)

while True:

    for event in pygame.event.get():
        if ((event.type == QUIT) or
            ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
            (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()

        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

    background.draw()

    oGame.draw()

    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)

def userInterface():
    print("Master Control Program\n\n")
    print("1-PULL Current Staged Repo\n")
    print("2-PUSH Current Staged Repo\n\n")
    choice = input("Please select>> ")
    
    if choice == str(1):
        warning1 = input("***WARNING***, the current activeStage will be deleted, do you want to continue? y/n >> ")
        if warning1.upper() == "Y":
            return 1
        else:
            return 0
    elif choice == str(2):
        return 2