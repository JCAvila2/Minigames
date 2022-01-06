import pygame, os, math, random, time


# Window Settings
pygame.init()
width = 1250
height = 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock, Paper or Scissors")
FPS = 150
refresh = pygame.time.Clock()


# Variables
winner = str()
input_user = str()
computer_input = str()
Ties = 0
user_score = 0
computer_score = 0
OPTIONS = ["rock", "paper", "scissors"]
check = False
round = 0

# Colors
background_color = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (135, 135, 135)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# Fonts
title_font = pygame.font.SysFont("comicsans", 55)
score_font = pygame.font.Font('freesansbold.ttf', 40)
buttons_font = pygame.font.SysFont("comicsans", 45)
words_font = pygame.font.SysFont("comicsans", 55)


# Load images
rock = pygame.image.load("rps/rock.png").convert_alpha()
paper = pygame.image.load("rps/paper.png").convert_alpha()
scissors = pygame.image.load("rps/scissors.png").convert_alpha()
quit_icon = pygame.image.load("icons/exit_button.PNG").convert_alpha()


# Create class for buttons
class Button():
    def __init__(self, x, y, image, scale):
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        global pos
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


# Buttons
button_rock = Button(200, 300, rock, 0.3)
button_paper = Button(570, 300, paper, 0.3)
button_scissors = Button(950, 300, scissors, 0.3)
button_quit = Button(10, 10, quit_icon, 0.1)

# Text
titulo = title_font.render("Choose:", True, (0, 0, 0))
vs = title_font.render("VS", True, BLACK)


# Loop for updating the window
window.fill(background_color)
window.blit(titulo, (520, 10))
run = True
while run:
    refresh.tick(FPS)

    # Buttons
    button_rock.draw()
    button_paper.draw()
    button_scissors.draw()
    button_quit.draw()


    for event in pygame.event.get(): # For loop to detect events 
        if event.type == pygame.QUIT: # If user clicks quit button of the window stop the loop
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # If user press "esc" stop the loop
                run = False
        if event.type == pygame.MOUSEBUTTONDOWN: # Detect if a button is clicked  
            if button_rock.draw():
                random_number = random.randint(0,2)
                computer_input = OPTIONS[int(random_number)]
                input_user = OPTIONS[0]
                check = True
            elif button_paper.draw():
                random_number = random.randint(0,2)
                computer_input = OPTIONS[int(random_number)]
                input_user = OPTIONS[1]
                check = True
            elif button_scissors.draw():
                random_number = random.randint(0,2)
                computer_input = OPTIONS[int(random_number)]
                input_user = OPTIONS[2] 
                check = True
            elif button_quit.draw():
                run = False
            else:
                check = False
                vacio = score_font.render("Choose an option", True, BLACK)
                window.blit(vacio, (450 , 650))

            # Win Conditions
            if check: # Check who is the winner if the user click an option button 
                round += 1
                # User wins
                if input_user == "rock" and computer_input == "scissors":                     
                    winner = "user"          
                elif input_user == "paper" and computer_input == "rock":
                    winner = "user"
                elif input_user == "scissors" and computer_input == "paper":
                    winner = "user"
                # Computer wins
                elif computer_input == "rock" and input_user == "scissors":
                    winner = "computer"
                elif computer_input == "paper" and input_user == "rock":
                    winner = "computer"    
                elif computer_input == "scissors" and input_user == "paper":
                    winner = "computer"   
                else: # If none of the conditions above are met, it is a tie
                    winner = "tie"

                def print_winner(): # Function to print in the window who is the winner
                    global user_score, computer_score, Ties
                    x = 520
                    y = 10
                    if winner == "user":
                        user_score += 1
                        window.fill(GREEN)
                        Windor = score_font.render("You Won!", True, BLACK)
                        window.blit(Windor, (x + 30, y))
                    elif winner == "computer":
                        computer_score += 1
                        window.fill(RED)
                        perdedor = score_font.render("You Lost", True, BLACK)
                        window.blit(perdedor, (x + 30, y))
                    elif winner == "tie":
                        Ties += 1
                        window.fill(GRAY)
                        Tie = score_font.render("Tie", True, BLACK)
                        window.blit(Tie, (x + 80, y))
                print_winner()

        
        def showInputUser():
            x = 320
            y = 50
            if input_user == OPTIONS[0]:
                showRock = pygame.transform.scale(rock, (225, 222))
                return window.blit(showRock, (x, y))
            elif input_user == OPTIONS[1]:
                showPaper = pygame.transform.scale(paper, (225, 222))
                return window.blit(showPaper, (x, y))
            elif input_user == OPTIONS[2]:
                showScissors = pygame.transform.scale(scissors, (225, 222))
                return window.blit(showScissors, (x, y))
            
        def showInputComputer():
            x = 720
            y = 50
            if computer_input == OPTIONS[0]:
                showRock = pygame.transform.scale(rock, (225, 222))
                return window.blit(showRock, (x, y))
            elif computer_input == OPTIONS[1]:
                showPaper = pygame.transform.scale(paper, (225, 222))
                return window.blit(showPaper, (x, y))
            elif computer_input == OPTIONS[2]:
                showScissors = pygame.transform.scale(scissors, (225, 222))
                return window.blit(showScissors, (x, y))
        
        def HUD(): # Function that shows the results of the games in real time
            # Choices
            user_choice = score_font.render("Player choice: " + str(input_user), True, BLACK)
            window.blit(user_choice, (450, 550))
            showInputUser()
            computer_choice = score_font.render("Computer choice: " + str(computer_input), True, BLACK)
            window.blit(computer_choice, (450, 600))
            showInputComputer()
            # Scores
            user_results = score_font.render("User score: " + str(user_score), True, BLACK)
            window.blit(user_results, (10, 550))
            computer_results = score_font.render("Computer score: " + str(computer_score), True, BLACK)
            window.blit(computer_results, (10, 600))
            Ties_show = score_font.render("Draws: " + str(Ties), True, BLACK)
            window.blit(Ties_show, (10, 650))
            total_rounds = score_font.render("Rounds: " + str(round), True, BLACK)
            window.blit(total_rounds, (950, 550))
            window.blit(vs, (600, 100))
        if round > 0:
            HUD()

    pygame.display.update()        
exec(open("main.py").read()) # Go back to "main.py"
