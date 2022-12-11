import pygame , sys
from button import Button
import time
import random
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN =(0,255,0)
BLUE = ( 0,0,255)
windown_shape= (800,600)
SCREEN = pygame.display.set_mode(windown_shape)
pygame.display.set_caption("Snake Game")
## fps 
fps = pygame.time.Clock()
##default pos snake 



## direction defaut 
snake_speed = 15


def get_font(size):
    return pygame.font.SysFont("time new roman",size)

score = 0
def show_score(choice,color,font,size):
    global score
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render("SCORE : " + str(score),True,color)
    score_rect = score_surface.get_rect()

    SCREEN.blit(score_surface,score_rect)

def game_over():
    
    myfont = pygame.font.SysFont('time new roman',50)
    game_over_surface = myfont.render("YOUR SCORE : " + str(score),True,RED)
    game_over_rect = game_over_surface.get_rect()

    game_over_rect.midtop = [windown_shape[0],windown_shape[1]]

    SCREEN.blit(game_over_surface,game_over_rect)
    pygame.display.flip()

    time.sleep(1)
    pygame.quit()

    quit()

def play():
    global score
    change_to = 'RIGHT'
    snake_pos = [windown_shape[0]/2,windown_shape[1]/2]
    snake_body = [[100,50],
                [90,50],
                [80,50],
                [70,50]]
    ## fruit pos 
    fruit_pos = [random.randrange(1,(windown_shape[0]//10) )*10,
            random.randrange(1,(windown_shape[1]//10))*10]
    fruit_spam = True 
    while True:
        Play_mouse_pos = pygame.mouse.get_pos()
        SCREEN.fill('Black')


        Play_back = Button(image=None,pos=(730,50),
                            text_input='Back',
                            font = get_font(75),base_color ='White',hovering_color ='Green')
        Play_back.changeColor(Play_mouse_pos)
        Play_back.update(SCREEN)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_back.checkForInput(Play_mouse_pos):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and change_to != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and change_to != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and change_to != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and change_to != 'LEFT': 
                    change_to = 'RIGHT'
        if change_to == 'UP':
            snake_pos[1] -= 10
        if change_to == 'DOWN':
            snake_pos[1] += 10
        if change_to == 'RIGHT':
            snake_pos[0] += 10
        if change_to == 'LEFT':
            snake_pos[0] -= 10  
        snake_body.insert(0,list(snake_pos))
        if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
            score += 10
            fruit_spam = False
        else:
            snake_body.pop()
        if not fruit_spam:
            fruit_pos = [random.randrange(1,(windown_shape[0]//10))*10,random.randrange(1,(windown_shape[1]//10))*10]
        fruit_spam = True
        ##SCREEN.fill(BLACK)

        for pos in snake_body:
            pygame.draw.rect(SCREEN,GREEN,pygame.Rect(pos[0],pos[1],10,10))
        pygame.draw.rect(SCREEN,WHITE,pygame.Rect(fruit_pos[0],fruit_pos[1],10,10))

        if snake_pos[0] < 0 or snake_pos[0] > windown_shape[0]:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > windown_shape[1]:
            game_over()
        for  block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()
        show_score(1,WHITE,'time new roman',20)
        pygame.display.update()
        fps.tick(snake_speed)


def main_menu():
    while True:
        SCREEN.fill('Black')
        Menu_mouse_pos = pygame.mouse.get_pos()
        Menu_text = get_font(100).render("Main menu", True,"#b68f40")
        Menu_rect = Menu_text.get_rect(center = (400,100))

        Play_button = Button(image = None,pos=(400,300),
                            text_input ="PLAY",font = get_font(75),base_color="#d7fcd4",hovering_color='White')
        Quit_button = Button (image=None,pos =(400,500),
                            text_input = "QUIT",font =get_font(75),base_color='#d7fcd4',hovering_color='White')
        SCREEN.blit(Menu_text,Menu_rect)

        for button in [Play_button,Quit_button]:
            button.changeColor(Menu_mouse_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_button.checkForInput(Menu_mouse_pos):
                    play()
                if Quit_button.checkForInput(Menu_mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()