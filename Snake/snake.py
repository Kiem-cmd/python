import pygame 
import random
import time
import sys
from button import *
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("SNAKE GAME")
font = pygame.font.SysFont("arialblack", 40)
TEXT_COL = (255,255,255)


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
## image
start_img = pygame.image.load("images/button_start.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
easy_img = pygame.image.load("images/button_easy.png").convert_alpha()
hard_img = pygame.image.load("images/button_hard.png").convert_alpha()
yes_img = pygame.image.load("images/button_yes.png").convert_alpha()
no_img = pygame.image.load("images/button_no.png").convert_alpha()

# ## 
start_button = Button(350,100, start_img, 1)
options_button = Button(345,250,options_img,1)
quit_button = Button(345,375,quit_img  , 1)
easy_button = Button(200,300, easy_img, 1)
hard_button = Button(445,300, hard_img, 1)
yes_button = Button(200, 450, yes_img, 1)
no_button = Button(500, 450, no_img, 1)



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
def draw_wall():
    pygame.draw.rect(screen,WHITE,[0,0,SCREEN_WIDTH,BLOCK_SIZE])
    pygame.draw.rect(screen,WHITE,[0,0,BLOCK_SIZE,SCREEN_HEIGHT])
    pygame.draw.rect(screen,WHITE,[0,SCREEN_HEIGHT - BLOCK_SIZE,SCREEN_WIDTH,BLOCK_SIZE])
    pygame.draw.rect(screen,WHITE,[SCREEN_WIDTH - BLOCK_SIZE,0,BLOCK_SIZE,SCREEN_HEIGHT])
# game_pause = True
def draw_snake(snake_list):
    for i in range(len(snake_list)):
        pygame.draw.rect(screen,WHITE,[snake_list[i][0],snake_list[i][1],BLOCK_SIZE,BLOCK_SIZE])
def draw_food(food_pos):
    pygame.draw.rect(screen,GREEN,[food_pos[0],food_pos[1], BLOCK_SIZE,BLOCK_SIZE])
def new_food():
    return [random.randrange(BLOCK_SIZE,SCREEN_WIDTH- BLOCK_SIZE,BLOCK_SIZE),random.randrange(BLOCK_SIZE,SCREEN_HEIGHT-BLOCK_SIZE,BLOCK_SIZE)]

def pause():
    pause = True 
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False

FPS = 20
score = 0
def game():
    global score
    status = "play"
    
    

    snake_list = [[SCREEN_WIDTH/2,SCREEN_HEIGHT/2]]
    snake_len = 1
    direction = 'right'

    food_pos = new_food()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause()
                elif event.key == pygame.K_LEFT and direction != 'right':
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    direction = 'right'
                elif event.key == pygame.K_UP and direction != 'down':
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':
                    direction = 'down'
        if direction == 'right': snake_list[0][0] += BLOCK_SIZE
        elif direction =='left': snake_list[0][0] -= BLOCK_SIZE
        elif direction == 'up':  snake_list[0][1] -= BLOCK_SIZE 
        elif direction =='down' : snake_list[0][1] += BLOCK_SIZE 


        if snake_list[0][0] == food_pos[0] and snake_list[0][1] == food_pos[1]:
            food_pos = new_food()
            score +=1
            snake_len +=1
            lenn = len(snake_list) - 1
            temp1 = [snake_list[lenn][0],snake_list[lenn][1]]
            temp2 = [snake_list[lenn-1][0],snake_list[lenn-1][1]]
            if direction =='right':
                snake_list.append([temp2[0]-temp1[0],temp1[1]])
            elif direction =='left':
                snake_list.append([temp2[0]+temp1[0],temp1[1]])
            elif direction =='up':
                snake_list.append([temp1[0],temp2[1] - temp1[1]])
            elif direction =='down':
                snake_list.append([temp1[0],temp1[1] + temp2[1]])
    
            


        if (snake_list[0][0] < BLOCK_SIZE                 \
            or snake_list[0][0] > SCREEN_WIDTH-BLOCK_SIZE \
            or snake_list[0][1] < BLOCK_SIZE               \
            or snake_list[0][1] > SCREEN_HEIGHT - BLOCK_SIZE):
            game_over()
        
        for i in range(1,len(snake_list)):
            if snake_list[0][0] == snake_list[i][0] and snake_list[0][1] == snake_list[i][1]:
                game_over()

        for i in range(len(snake_list) -1 ,0, -1):
            snake_list[i][0] = snake_list[i-1][0]
            snake_list[i][1] = snake_list[i-1][1]

        screen.fill(BLACK)
        draw_wall()
        draw_snake(snake_list)
        draw_food(food_pos)
        score_text = font.render("Score: " + str(score), True, (75, 120, 175))
        screen.blit(score_text, (20,20))
        pygame.display.update()
        clock.tick(FPS)
def option():
    global FPS
    screen.fill((52,78,91))
    while True:
        screen.fill((52,78,91))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if easy_button.draw(screen):
            FPS = 10
            start()
        if hard_button.draw(screen):
            FPS = 29
            start()
        pygame.display.update()

def start():
    global FPS 
    screen.fill((52,78,91))
    while True:
        if start_button.draw(screen):
            game()
        if options_button.draw(screen):
            option()
        if quit_button.draw(screen):
            pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

def game_over():
    global score
    global FPS
    while True:
        screen.fill((52,78,91))
        text = font.render("Score: " + str(score) + "-Do you want play again ? ", True, (255,0,0))
        screen.blit(text, (50,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if yes_button.draw(screen):
            score = 0
            FPS = 10
            start()
        if no_button.draw(screen):
            pygame.quit()
            sys.exit()
        pygame.display.update()   
start()

