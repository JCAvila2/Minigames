import pygame, os, math, random, time, json


# Settings of the window
screenWidth = 1250
screenHeight = 720
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Mini-games")
pygame.init()


# Load images
exitButon = pygame.image.load("icons/exit_button.png").convert_alpha()
hangmanButton = pygame.image.load("icons/hangman_logo.png").convert_alpha()
tttButon = pygame.image.load("icons/ttt_icon.png").convert_alpha()
rpsButon = pygame.image.load("icons/ppt.png").convert_alpha()


# Class for buttons
class Button():
    def __init__(self, x, y, image, scale):
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        window.blit(self.image, (self.rect.x, self.rect.y))
        return action


# Fonts
title_font = pygame.font.Font("freesansbold.ttf", 55)
buttons_font = pygame.font.SysFont("comicsans", 45)


# Buttons
button_hangman = Button(200, 300, hangmanButton, 0.3)
button_rps = Button(515, 285, rpsButon, 0.28)
button_ttt = Button(900, 300, tttButon, 0.3)
button_exit = Button(50, 600, exitButon, 0.1)


# Text
Title = title_font.render("What do you want to play? ", True, (0, 0, 0))
    

# Loop for updating the window
run = True
while run:
    window.fill((255, 255, 255))
    window.blit(Title, (270, 30))

    # Conditions to open games
    if button_hangman.draw(): # If hangman button gets clicked, execute "hangman.py"
        exec(open("games\\hangman.py").read())
    elif button_rps.draw(): # If Rock, Paper and Scissors button gets clicked, execute "rps.py"
        exec(open("games\\rps.py").read())
    elif button_ttt.draw(): # If Tic Tac Toe button gets clicked, execute "ttt.py"
        exec(open("games\\ttt.py").read())

    # Conditions to close the window
    elif button_exit.draw():
        run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
