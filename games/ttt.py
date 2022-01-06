import pygame, os, math, random, time


# Window settings
pygame.init()
width = 1250
height = 720
window = pygame.display.set_mode((width, height))
FPS = 150
refresh = pygame.time.Clock()
pygame.display.set_caption("Tic tac toe")
board = [["     ", "     ", "     "], ["     ", "     ", "     "], ["     ", "     ", "     "]]


# Variables
clicked = True
round = 0
pos_mouse = pygame.mouse.get_pos()    
winner = " "


# Colors
background_color = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)


# Fonts
title_font = pygame.font.SysFont("comicsans", 55)
buttons_font = pygame.font.SysFont("comicsans", 77) 
words_font = pygame.font.SysFont("comicsans", 55) 
score_font = pygame.font.Font('freesansbold.ttf', 65)


# Images
menu = pygame.image.load("icons/exit_button.PNG").convert_alpha()
boardImage = pygame.image.load("icons/boardttt.png").convert_alpha()


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


def button_ttt(window, position, text):
    button_text_color = BLACK 
    button_background_color = background_color 
    type_text = buttons_font.render(text, 1, button_text_color)
    x, y, w, h = type_text.get_rect()
    x, y = position
    pygame.draw.line(window, (250, 250, 250), (x, y), (x + w, y), 0)
    pygame.draw.line(window, (250, 250, 250), (x, y - 2), (x, y + h), 0)
    pygame.draw.line(window, (50, 50, 50), (x, y + h), (x + w, y + h), 0)
    pygame.draw.line(window, (50, 50, 50), (x + w, y + h), [x + w, y], 0)
    pygame.draw.rect(window, button_background_color, (x, y, w, h))
    return window.blit(type_text, (x, y)) 


def ttt_draw(): # Draw the buttons
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, menuButton
    b1 = button_ttt(window, (450, 200), board[0][0])
    b2 = button_ttt(window, (575, 200), board[0][1])
    b3 = button_ttt(window, (700, 200), board[0][2])
    b4 = button_ttt(window, (450, 330), board[1][0])
    b5 = button_ttt(window, (575, 330), board[1][1])
    b6 = button_ttt(window, (700, 330), board[1][2])
    b7 = button_ttt(window, (450, 450), board[2][0])
    b8 = button_ttt(window, (575, 450), board[2][1])
    b9 = button_ttt(window, (700, 450), board[2][2])
    menuButton = Button(30, 30, menu, 0.1) # Menu button


run = True
while run:
    refresh.tick(FPS)
    window.fill(background_color)
    def image(): # Board update function 
        ttt_draw()
        window.blit(boardImage, (450, 200))
    image()
    menuButton.draw() # Menu button    

    for event in pygame.event.get(): #For loop to detect events
        if (event.type == pygame.QUIT): # If user clicks quit button of the window stop the loop
            exec(open("main.py").read())
        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE: # If user press "esc" stop the loop
                exec(open("main.py").read())
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menuButton.draw():
                exec(open("main.py").read())

            def fill_board():
                global board, clicked, round
                #Button 1
                if b1.collidepoint(pygame.mouse.get_pos()) and board[0][0] == "     " and clicked == True:
                    board[0][0] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b1.collidepoint(pygame.mouse.get_pos()) and board[0][0] == "     " and clicked == False:
                    board[0][0] = " O "
                    image()
                    clicked = True
                    round += 1
                #Button 2
                elif b2.collidepoint(pygame.mouse.get_pos()) and board[0][1] == "     " and clicked == True:
                    board[0][1] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b2.collidepoint(pygame.mouse.get_pos()) and board[0][1] == "     " and clicked == False:
                    board[0][1] = " O "
                    image()
                    clicked = True
                    round += 1
                #Button 3
                elif b3.collidepoint(pygame.mouse.get_pos()) and board[0][2] == "     " and clicked == True:
                    board[0][2] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b3.collidepoint(pygame.mouse.get_pos()) and board[0][2] == "     " and clicked == False:
                    board[0][2] = " O "
                    image()
                    clicked = True
                    round += 1
                #Button 4
                elif b4.collidepoint(pygame.mouse.get_pos()) and board[1][0] == "     " and clicked == True:
                    board[1][0] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b4.collidepoint(pygame.mouse.get_pos()) and board[1][0] == "     " and clicked == False:
                    board[1][0] = " O "
                    image()
                    clicked = True
                    round += 1
                #Button 5
                elif b5.collidepoint(pygame.mouse.get_pos()) and board[1][1] == "     " and clicked == True:
                    board[1][1] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b5.collidepoint(pygame.mouse.get_pos()) and board[1][1] == "     " and clicked == False:
                    board[1][1] = " O "
                    image()
                    clicked = True
                    round += 1
                #Button 6
                elif b6.collidepoint(pygame.mouse.get_pos()) and board[1][2] == "     " and clicked == True:
                    board[1][2] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b6.collidepoint(pygame.mouse.get_pos()) and board[1][2] == "     " and clicked == False:
                    board[1][2] = " O "
                    image()
                    clicked = True
                    round += 1
                #Button 7
                elif b7.collidepoint(pygame.mouse.get_pos()) and board[2][0] == "     " and clicked == True:
                    board[2][0] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b7.collidepoint(pygame.mouse.get_pos()) and board[2][0] == "     " and clicked == False:
                    board[2][0] = " O "
                    image()
                    clicked = True
                    round += 1
                #Button 8
                elif b8.collidepoint(pygame.mouse.get_pos()) and board[2][1] == "     " and clicked == True:
                    board[2][1] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b8.collidepoint(pygame.mouse.get_pos()) and board[2][1] == "     " and clicked == False:
                    board[2][1] = " O "
                    image()
                    clicked = True
                    round += 1
                #Button 9
                elif b9.collidepoint(pygame.mouse.get_pos()) and board[2][2] == "     " and clicked == True:
                    board[2][2] = " X "
                    image()
                    clicked = False
                    round += 1
                elif b9.collidepoint(pygame.mouse.get_pos()) and board[2][2] == "     " and clicked == False:
                    board[2][2] = " O "
                    image()
                    clicked = True
                    round += 1
            fill_board()

            
            def w_condition(board, round): # Win conditions
                global run, winner
                # Win conditions for X:
                def end_game_X(): 
                    global winner, run
                    winner = "X"
                    run = False
                #X wins horizontally 
                if board[0][0] == " X " and board[0][1] == " X " and board[0][2] == " X ":
                    pygame.draw.line(window, RED, (420, 255), (850, 255), 20)
                    end_game_X()
                elif board[1][0] == " X " and board[1][1] == " X " and board[1][2] == " X ":
                    pygame.draw.line(window, RED, (420, 385), (850, 385), 20)
                    end_game_X()
                elif board[2][0] == " X " and board[2][1] == " X " and board[2][2] == " X ":
                    pygame.draw.line(window, RED, (420, 500), (850, 500), 20)
                    end_game_X()
                #X wins vertically 
                elif board[0][0] == " X " and board[1][0] == " X " and board[2][0] == " X ":
                    pygame.draw.line(window, RED, (500, 200), (500, 565), 20)
                    end_game_X()
                elif board[0][1] == " X " and board[1][1] == " X " and board[2][1] == " X ":
                    pygame.draw.line(window, RED, (630, 200), (630, 565), 20)
                    end_game_X()
                elif board[0][2] == " X " and board[1][2] == " X " and board[2][2] == " X ":
                    pygame.draw.line(window, RED, (755, 200), (755, 565), 20)
                    end_game_X()
                #X wins diagonal 
                elif board[0][0] == " X " and board[1][1] == " X " and board[2][2] == " X ":
                    pygame.draw.line(window, RED, (450, 200), (805, 565), 20)
                    end_game_X()
                elif board[0][2] == " X " and board[1][1] == " X " and board[2][0] == " X ":
                    pygame.draw.line(window, RED, (805, 200), (450, 565), 20)
                    end_game_X()
                
                # Win conditions for O:
                def end_game_O():
                    global winner, run
                    winner = "O"  
                    run = False
                #O wins horizontally
                if board[0][0] == " O " and board[0][1] == " O " and board[0][2] == " O ":
                    pygame.draw.line(window, RED, (420, 250), (850, 250), 20)
                    end_game_O()
                elif board[1][0] == " O " and board[1][1] == " O " and board[1][2] == " O ":
                    pygame.draw.line(window, RED, (420, 385), (850, 385), 20)
                    end_game_O()
                elif board[2][0] == " O " and board[2][1] == " O " and board[2][2] == " O ":
                    pygame.draw.line(window, RED, (420, 500), (850, 500), 20)
                    end_game_O()
                #O wins vertically
                elif board[0][0] == " O " and board[1][0] == " O " and board[2][0] == " O ":
                    pygame.draw.line(window, RED, (500, 200), (500, 565), 20)
                    end_game_O()
                elif board[0][1] == " O " and board[1][1] == " O " and board[2][1] == " O ":
                    pygame.draw.line(window, RED, (630, 200), (630, 565), 20)
                    end_game_O()
                elif board[0][2] == " O " and board[1][2] == " O " and board[2][2] == " O ":
                    pygame.draw.line(window, RED, (755, 200), (755, 565), 20)
                    end_game_O()
                #O wins diagonal
                elif board[0][0] == " O " and board[1][1] == " O " and board[2][2] == " O ":
                    pygame.draw.line(window, RED, (450, 200), (805, 565), 20)
                    end_game_O()
                elif board[0][2] == " O " and board[1][1] == " O " and board[2][0] == " O ":
                    pygame.draw.line(window, RED, (805, 200), (450, 565), 20)
                    end_game_O()
                # If neither X nor O win in 9 rounds, it is a draw 
                elif round == 9 and winner != "X" and winner != "O":
                    winner = "Tie"
                    run = False
            w_condition(board, round)
       
    # Conditional to know whose turn it is  
    if clicked:
        user = "X"
    elif clicked == False:
        user = "O"

    if winner == " ":
        turno = score_font.render("Turn of: " + str(user), True, BLACK) 
        window.blit(turno, (450, 30))

    pygame.display.update()
# Show Results 
if winner == "Tie":
    Tie = score_font.render("Tie...", True, BLACK) 
    window.blit(Tie, (570, 30))
    run = False
elif winner == "X":
    x_w = score_font.render("Player X Won", True, BLACK) 
    window.blit(x_w, (420, 30))
    run = False
elif winner == "O":
    o_w = score_font.render("Player O Won", True, BLACK) 
    window.blit(o_w, (420, 30))
    run = False

pygame.display.update()
time.sleep(3)
exec(open("main.py").read())
