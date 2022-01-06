import pygame, os, math, random, time, json


#Window settings
pygame.init()
width = 1250
height = 720
cenx = (1250/2)
ceny = (720/2)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hangman")
FPS = 150
refresh = pygame.time.Clock()
run = True


# Words to guess
list_of_words = json.load(open("Hangman\simpleDictionary.json"))
chosen_word = random.choice(list_of_words).upper()
guessed = list()
show_letter = str()
health_points = 6


draws = list() # Create list of images
draws_status = 0 # Order of draws

# Load Images and append to "draws" list
draws.append(pygame.image.load("Hangman\hangman0.png"))
draws.append(pygame.image.load("Hangman\hangman1.png"))
draws.append(pygame.image.load("Hangman\hangman2.png"))
draws.append(pygame.image.load("Hangman\hangman3.png"))
draws.append(pygame.image.load("Hangman\hangman4.png"))
draws.append(pygame.image.load("Hangman\hangman5.png"))
draws.append(pygame.image.load("Hangman\hangman6.png"))

heart = (pygame.image.load("Hangman\heart.png"))
heart = pygame.transform.scale(heart, (100, 100))

menu = pygame.image.load("icons/exit_button.PNG").convert_alpha()
    

# Colors
background_color = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


# Fonts
letters_font = pygame.font.SysFont("comicsans", 40) 
words_font = pygame.font.SysFont("comicsans", 55)
buttons_font = pygame.font.SysFont("comicsans", 45)
score_font = pygame.font.Font('freesansbold.ttf', 65)
title_font = pygame.font.Font('freesansbold.ttf', 45)


# Text
title = letters_font.render("Guess a letter:", True, BLACK)
winner_alert = letters_font.render("You win!", True, BLACK)
loser_alert = letters_font.render("You Lost!", True, BLACK)


def letters_buttons(): # Bottons of letters
    global radio, space, letters, initialX, initialY, A
    radio = 30
    space = 25
    letters = list()
    initialX = round((width - (radio * 2 + space) * 14) / 2)
    initialY = 500
    A = 65
    for i in range(26): # Loop for making the 26 letters
        x = initialX + space * 2 + (radio * 2 + space) * (i % 13)
        y = initialY + ((i // 13) * (space + radio * 2))
        letters.append([x, y, chr(A + i), True])

letters_buttons()    


def refresh_letters(show_letter): # Refresh letters guessed
    global guessed
    window.fill(background_color)
    
    #Draw buttons
    for letra in letters:
        x, y, ltr, visible = letra
        if visible:
            text = letters_font.render(ltr, 1, BLACK)
            pygame.draw.circle(window, BLACK, (x,y), radio, 3)      
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # Condition for replace or not the guessed letter
    for letra in chosen_word:
        if letra in guessed:
            show_letter += letra + " "            
        else: 
            show_letter += "_ "
    
    text = words_font.render(show_letter, 1, BLACK)
    window.blit(text,(500,200))


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


# Button go back to menu
menuButton = Button(30, 30, menu, 0.1) 


# Loop for refreshing the window
while run:
    refresh.tick(FPS)
    refresh_letters(show_letter) # Buttons of letters
    window.blit(draws[draws_status], (200, 130)) # Hangman draw (updates when player lose an hp)
    menuButton.draw() # Button go back to menu


    # Show health points   
    hp = letters_font.render(str(health_points), True, BLACK)
    window.blit(heart, (1100, 20)) # Heart draw
    window.blit(hp, (1140, 35)) # HP count


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # End the loop and go back to main menu if user click on quit button of the window
            exec(open("main.py").read())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # End the loop and go back to main menu if user press "esc"
                exec(open("main.py").read())
        if event.type == pygame.MOUSEBUTTONDOWN: # Conditions for clicks
            position_mouse_x, position_mouse_y = pygame.mouse.get_pos() # Variables with the position of the mouse          
            if menuButton.draw(): # End the loop and go back to main menu if user click menu button
                exec(open("main.py").read())
            for letter in letters: # For loop to give functionality to the letters
                x, y, ltr, visible = letter                               
                if visible:
                    distance = math.sqrt((x - position_mouse_x) ** 2 + (y - position_mouse_y) ** 2)
                    if distance < radio:
                        guessed.append(ltr)
                        letter[3] = False
                        if ltr in chosen_word: # If the letter guessed for the user is in the chosen word change the background color to green                      
                            background_color = GREEN 
                            window.fill(background_color) 
                        elif ltr not in chosen_word: # If the letter guessed for the user is NOT in the chosen word change the background color to red 
                            draws_status += 1
                            health_points -= 1
                            background_color = RED
                            window.fill(background_color)
            

    # Show messages depending on the background color  
    if background_color == GREEN:
        Windor = score_font.render(str("You got it right, go on!"), True, (255, 255, 255))
        window.blit(Windor, (cenx - 300, 40))
    elif background_color == RED:
        perdedor = score_font.render(str("Ups... you miss"), True, (255, 255, 255))
        window.blit(perdedor, (cenx - 230, 40))
    else:
        none = title_font.render(str("Guess a letter:"), True, BLACK)
        window.blit(none, (cenx - 150, 40))
                         
    pygame.display.update()

    def win(): # Win/lost conditions and messages
        global run, background_color
        victory = True
        for letra in chosen_word:
            if letra not in guessed:
                victory = False
                break
            
        if victory:
            background_color = GREEN   
            Windor = buttons_font.render("You Won!", True, (255, 255, 255))
            window.fill(background_color)
            window.blit(Windor, (500, 300))                    
            run = False

        elif draws_status == 7:
            word = score_font.render(chosen_word, True, (255, 255, 255))
            message = buttons_font.render("You lost, the word was:", True, (255, 255, 255))
            background_color = RED
            window.fill(background_color)
            window.blit(word, (500, 300))
            window.blit(message, (400, 200))
            run = False
    win()


pygame.display.update()
time.sleep(3) # Stop the execution for 3 seconds while showing the results
exec(open("main.py").read()) # Execute "main.py"
