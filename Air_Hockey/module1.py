import pygame
import airhockey
from airhockey import*
pygame.mixer.init()
#import game
pygame.init()
display_width = 900
display_height = 600
# DEFINING COLOURS
black = (0,0,0)
new = (238,64,0)
orange = (150,150,150)
lig_orange = (200,250,0)
light_blue = (100,150,250)
red = (255,0,50)

#Surface of the game
airhockey = pygame.display.set_mode((display_width,display_height))
pygame.mixer.music.load('./sounds/background.ogg')
pygame.mixer.music.play(-1)
#Defining the fonts
font = pygame.font.SysFont('Taped Up Tight',100)
medfont = pygame.font.SysFont('Garuda',350)
smallfont = pygame.font.SysFont('Garuda',30)
largefont = pygame.font.SysFont('Garuda',90)
def surface():
    pygame.display.set_caption("AIR HOCKEY") #Naming the game
    airhockey.fill(light_blue)               #filling the backgroung colour
    message_to_screen("AIR HOCKEY",red,[display_width/15,display_height/12])
    bgd_image = pygame.image.load("images/rsz_board2.jpg")
    airhockey.blit(bgd_image,[display_width*0.62,0])
    button("play",100,300,100,40,orange,lig_orange,action = "play")
    button("help",100,400,100,40,orange,lig_orange,action = "help")
    button("quit",100,500,100,40,orange,lig_orange,action = "quit")
def game_controls():
    g_cont = True
    while g_cont is True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT ):
                 pygame.quit()
                 quit()
        text_button("PLAYER_1",new,225,150,300,40,size = "small")
        text_button("UP     :UP Arrow",black,225,185,300,40,size = "small")
        text_button("RIGHT : RIGHT Arrow",black,225,220,300,40,size = "small")
        text_button("DOWN  : DOWN Arrow",black,225,255,300,40,size = "small")
        text_button("LEFT  : LEFT Arrow",black,225,290,300,40,size = "small")
        text_button("PLAYER_2",new,225,350,300,40,size = "small")
        text_button("UP  : KEY_W",black,225,385,300,40,size = "small")
        text_button("DOWN  : KEY_S",black,225,420,300,40,size = "small")
        text_button("LEFT  : KEY_A",black,225,455,300,40,size = "small")
        text_button("RIGHT  : KEY_D",black,225,490,300,40,size = "small")
        text_button("SCORE 10 GOALS TO WIN",(255,0,0),100,550,300,40,size = "small")
        button("play",100,300,100,40,orange,lig_orange,action = "play")
        button("help",100,400,100,40,orange,lig_orange,action = None)
        button("quit",100,500,100,40,orange,lig_orange,action = "quit")
        pygame.display.update()

def button(text,x,y,width,height,c1,c2,action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if( x+width > cur[0]>x and y+height > cur[1] >y):
        pygame.draw.rect(airhockey,c1,(x,y,width,height))
        if(click[0] == 1 and action != None):
            if(action == "quit"):
                pygame.quit()
                quit()
            if(action == "help"):
                game_controls()
            if(action == "play"):
                run()
    else:
        pygame.draw.rect(airhockey,c2,(x,y,width,height))
    text_button(text,black,x,y,width,height)

def text_objects(text,colour,size = "small"):
    if(size == "small"):
        textsurface = smallfont.render(text,True,colour)
    if(size == "medium"):
        textsurface = medfont.render(text,True,colour)
    if(size == "large"):
        textsurface = largefont.render(text,True,colour)
    return textsurface,textsurface.get_rect()

def text_button(msg,colour,button_x,button_y,B_width,B_height,size = "small"):
    textSurf,textRect =text_objects(msg,colour,size)
    textRect.center =(button_x+(B_width/2),button_y+(B_height/2))
    airhockey.blit(textSurf,textRect)


def message_to_screen(message,colour,position):
    screen_text = font.render(message,True,colour)
    airhockey.blit(screen_text,position)

game_play = True
while game_play is True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT ):
             game_play = False
    surface()
    pygame.display.update()
pygame.quit()
quit()
