import pygame 
import pygame_gui
import numpy as np
pygame.init()
Width,Height = (600,600)
WHITE = (255,255,255)
x_image = pygame.image.load('X.png')
x_image = pygame.transform.scale(x_image,(150,150))
o_image = pygame.image.load('O.png')
o_image = pygame.transform.scale(o_image,(150,150))


screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("TIC TAC TOE")





pygame.draw.line(screen,WHITE,(0,0),(Width,0),5)
pygame.draw.line(screen,WHITE,(Width,0),(Width,Height),5)
pygame.draw.line(screen,WHITE,(0,Height),(Width,Height),5)
pygame.draw.line(screen,WHITE,(0,0),(0,Height),5)

pygame.draw.line(screen,WHITE,(Width/3,0),(Width/3,Height),5)
pygame.draw.line(screen,WHITE,(2*Width/3,0),(2*Width/3,Height),5)
pygame.draw.line(screen,WHITE,(0,(Height)/3),(Width,(Height)/3),5)
pygame.draw.line(screen,WHITE,(0,2*(Height)/3),(Width,2*(Height)/3),5)

board = np.array([ [0,0,0],
                   [0,0,0],
                   [0,0,0]])


player = 1
pygame.display.update()
 
running = True


def draw_image():
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if(board[row,col] == 1):
                screen.blit(x_image,(col*Width/3+20,row*(Height)/3 + 20))
            if(board[row,col] == 2):
                screen.blit(o_image,(col*Width/3+20,row*(Height)/3 + 20))
    pygame.display.flip()

win_array = [[(0,0),(0,1),(0,2)],
                     [(1,0),(1,1),(1,2)],
                     [(2,0),(2,1),(2,2)],
                     [(0,0),(1,0),(2,0)],
                     [(0,1),(1,1),(2,1)],
                     [(0,2),(1,2),(2,2)],
                     [(0,0),(1,1),(2,2)],
                     [(0,2),(1,1),(2,0)]]

def check_win():
    global board
    for i in win_array:
        b = [board[j] for j in i]
        if(len(set(b)) == 1 and b[0] != 0 and b[0] != 3):
            pygame.draw.line(screen,WHITE,(i[0][1] * Width/3 + 100,i[0][0] * (Height)/3 + 100 ),(i[2][1] * Width/3 + 100,i[2][0] * (Height)/3 + 100),8)
            for i in range(board.shape[0]):
                for j in range(board.shape[1]):
                    if(board[i][j] == 0):
                        board[i][j] = 3
            pygame.display.flip()
        
def play():
    global player
    global running 
    global board
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if(mouse_pos[0] < Width/3 and mouse_pos[1] < (Height)/3 and board[0,0] == 0 ):
                        board[0,0] = player
                        player = player ^ 3

                    elif(mouse_pos[0] < 2*Width/3 and mouse_pos[1] < (Height)/3 and Width/3<mouse_pos[0] and board[0,1] == 0):
                        board[0,1] = player
                        player = player ^ 3
                    elif(mouse_pos[0] < Width and mouse_pos[1] < (Height)/3 and 2*Width/3<mouse_pos[0] and board[0,2] == 0):
                        board[0,2] = player
                        player = player ^ 3
                    elif(mouse_pos[0] < Width/3  and mouse_pos[1] > (Height)/3 and mouse_pos[1]< 2*(Height)/3 and board[1,0] == 0):
                        board[1,0] = player
                        player = player ^ 3
                    elif(mouse_pos[0] > Width/3 and mouse_pos[1] > (Height)/3 and mouse_pos[0] < 2*Width/3 and mouse_pos[1] < 2*(Height)/3 and board[1,1] == 0):
                        board[1,1] = player
                        player = player ^ 3
                    elif(mouse_pos[0] < Width and mouse_pos[0] > 2*Width/3 and mouse_pos[1] < 2*(Height)/3 and mouse_pos[1] > (Height)/3 and board[1,2] == 0):
                        board[1,2] = player
                        player = player ^ 3
                    elif(mouse_pos[0] < Width/3 and mouse_pos[1] < (Height) and mouse_pos[1] > 2*(Height)/3 and board[2,0] == 0):
                        board[2,0] = player
                        player = player ^ 3
                    elif(mouse_pos[0] < 2*Width/3 and mouse_pos[1] > 2*(Height)/3 and mouse_pos[0] > Width/3 and mouse_pos[1] < (Height) and board[2,1] == 0):
                        board[2,1] = player
                        player = player ^ 3
                    elif(mouse_pos[0] < Width and mouse_pos[1] < (Height) and mouse_pos[0] > 2*Width/3 and mouse_pos[1] > 2*(Height)/3 and board[2,2] == 0):
                        board[2,2] = player
                        player = player ^ 3
        
                draw_image()
                check_win()           
            if event.type == pygame.QUIT:
                running = False

play()





