import pygame,sys
import module1 as P2

from pygame.locals import*
import math
import time

def run():
    pygame.init()
    clock = pygame.time.Clock()
    WHITE = (255,255,255)
    BLUE = (56,142,142)
    black = (0,0,0)
    screen = pygame.display.set_mode((800,700))
    pygame.display.set_caption('Air Hockey')
    score = 0
    #pygame.mixer.music.load('collision.wav')
    def distance(x1,x2,y1,y2):
    	return math.hypot(x2 - x1, y2 - y1)

    #A class to create the background.

    class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
    # A class to create the paddles.
    class Paddle(pygame.sprite.Sprite):
    	def __init__(self,image_file,location):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.centerx,self.rect.centery = location
            self.dx = 1 #self.score = 0
            self.dy= 1
     	#Functions to assign keys to handle the paddle.
	def Handle_keys_1(self):
            key = pygame.key.get_pressed()
            distance = 4
            if key[pygame.K_DOWN]:
                self.rect.centery += distance
            elif key[pygame.K_UP]:
                self.rect.centery -= distance
            elif key[pygame.K_RIGHT]:
                self.rect.centerx += distance
            elif key[pygame.K_LEFT]:
                self.rect.centerx -= distance


     	def Handle_keys_2(self):
    		key = pygame.key.get_pressed()
    		distance = 4
    		if key[pygame.K_s]:
                    self.rect.centery += distance
    		elif key[pygame.K_w]:
                    self.rect.centery -= distance
    		elif key[pygame.K_d]:
                    self.rect.centerx += distance
    		elif key[pygame.K_a]:
                    self.rect.centerx -= distance
     	# Function to make sure the paddle doesn't move out of the screen.
	def Restrict_bound_1(self):
    		if self.rect.centerx<0 + 20 + 25:
    			self.rect.centerx = 0 + 20 + 25
    		if self.rect.centerx>500 - 60 - 25  :
    			self.rect.centerx = 500 - 60 - 25
    		if self.rect.centery<350 + 25 :
    			self.rect.centery = 350 + 25
    		if self.rect.centery>700 - 20 -25 :
    			self.rect.centery = 700 - 20 -25

     	def Restrict_bound_2(self):
    		if self.rect.centerx<0 + 20 + 25:
    			self.rect.centerx = 0 + 20 + 25
    		if self.rect.centerx>500 - 60 - 25 :
    			self.rect.centerx = 500 - 60 - 25
    		if self.rect.centery>350 - 25 :
    			self.rect.centery = 350 - 25
    		if self.rect.centery<0 + 20 + 25 :
    			self.rect.centery = 0 + 20 + 25

    # A class to create the puck.
    class Puck(pygame.sprite.Sprite):

    	def __init__(self,image_file,location,change_y = 10 , change_x = 10):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.centerx,self.rect.centery = location
            self.dx = 0
            self.dy = 4
            self.score_1 = 0
            self.score_2 = 0
            self.score_comp_1 = 0
            self.score_comp_2 = 0

	#Function to make sure the puck doesn't move out of the screen.
    	def update_puck(self):
            if self.rect.centerx < 0 + 20 +15 :
                #pygame.mixer.music.play()
                self.rect.centerx = 35
                self.dx *= -1
            elif self.rect.centerx > 500 - 15 - 60 :
                #pygame.mixer.music.play()
                self.rect.centerx = 500 - 15 - 60
                self.dx *= -1
            if self.rect.centery < 0 + 20 + 15 :
                #pygame.mixer.music.play()
                self.rect.centery = 35
                self.dy *= -1
            elif self.rect.centery > 700 - 15 - 18 :
                #pygame.mixer.music.play()
                self.rect.centery = 700 - 15 -20
                self.dy *= -1
        #Limiting the speed of the puck.
	def limit_speed(self):
            if self.dx > 9 :
                self.dx = 9
            if self.dx <-9 :
                self.dx = -8
            if self.dy > 9 :
                self.dy = 9
            if self.dy <-9 :
                self.dy = -9
    	def reset(self):

		if(145 < self.rect.centerx < 320):
                    if(self.rect.centery <= 12 or self.rect.centery >= 685 ):
                        self.rect.centerx = 250
			self.rect.centery = 350
			self.dy = 4
			self.dx = 0

	# Keeping track of the players' score.
        def player_score(self):
            if(158 < self.rect.centerx < 325):
                if(self.rect.centery <= 34 ):
                    self.rect.centerx = 250
	            self.rect.centery = 350
                    self.score_1 += 1
                    self.dy = 3
                    self.dx = 0
		    time.sleep(3)


	        if(self.rect.centery >= 670):
                    self.rect.centery = 250
		    self.rect.centerx = 348
                    self.score_2 += 1
                    self.dy = 3
		    self.dx = 0
                    time.sleep(3)

    #Displaying the scores.
    def score_message(score_1,score_2):
        P2.text_button("PLAYER_1",black,500,150,300,40,size = "small")
        P2.text_button(score_1,black,500,180,300,40,size = "small")
        P2.text_button("PLAYER_2",black,500,400,300,40,size = "small")
        P2.text_button(score_2,black,500,440,300,40,size = "small")
        P2.message_to_screen(score_1,black,[500,150])
        P2.message_to_screen(score_2,black,[500,400])

    # Function to check collision between two sprites.
    def Check_collision(sprite1,sprite2):
        if(distance(sprite1.rect.centerx,sprite2.rect.centerx,sprite1.rect.centery,sprite2.rect.centery) <= 50):
            return True
        return False

    BackGround = Background('./images/board_1.png', [0,0])  #here is also changed
    paddle1 = Paddle('./images/paddle1.png',[250,525])
    paddle2 = Paddle('./images/paddle2.png',[250,175])
    puck = Puck('./images/puck.png',[250,350])
    game_run = True
    while game_run is True :
    	for event in pygame.event.get():

            if event.type == pygame.QUIT :
                pygame.quit()
		sys.exit()
    	screen.fill(BLUE)
    	screen.blit(BackGround.image, BackGround.rect)
    	paddle1.Handle_keys_1()
    	screen.blit(paddle1.image, paddle1.rect)
    	paddle1.Restrict_bound_1()
    	paddle2.Handle_keys_2()
    	screen.blit(paddle2.image,paddle2.rect)
    	paddle2.Restrict_bound_2()
    	screen.blit(puck.image,puck.rect)

        puck.score_comp_1 = puck.score_1
        puck.score_comp_2 = puck.score_2
        if Check_collision(puck,paddle1) :
            #pygame.mixer.music.play()
            puck.dx = -1 * puck.dx
            puck.dy = -1 * puck.dy
            puck.rect.centerx += puck.dx
            puck.rect.centery += puck.dy
            puck.rect.centery += puck.dy
            puck.rect.centerx += puck.dx
            puck.rect.centery += puck.dy
            puck.rect.centerx += puck.dx
            time.sleep(0.03)
            paddle1.rect.centery += 5

    	if Check_collision(puck,paddle2) :
            #pygame.mixer.music.play()
            puck.dx = -1*puck.dx + paddle2.dx
            puck.dy = -1*puck.dy + paddle2.dy
            puck.rect.centerx += puck.dx
            puck.rect.centery += puck.dy
            puck.rect.centery += puck.dy
            puck.rect.centerx += puck.dx
            puck.rect.centery += puck.dy
            puck.rect.centerx += puck.dx
            time.sleep(0.03)
            paddle2.rect.centery -= 5
        puck.limit_speed()
        puck.player_score()
        if(puck.score_2 == 10):
            P2.text_button("PLAYER_2 WON",(176,23,31),500,290,300,40,size = "small")
            P2.message_to_screen("game ",(255,0,0),[70,300])
            P2.message_to_screen("over ",(255,255,0),[250,300])
            game_run = False
        if(puck.score_1 == 10):
            P2.text_button("PLAYER_1 WON",(0,0,128),475,290,300,40,size = "small")
            P2.message_to_screen("game ",(0,255,255),[70,300])
            P2.message_to_screen("over ",(0,255,0),[250,300])
            game_run = False

    	puck.update_puck()
    	puck.rect.centery += puck.dy
    	puck.rect.centerx += puck.dx
        score_message(str(puck.score_1),str(puck.score_2))

        pygame.display.update()
    	clock.tick(60)
    pygame.display.update()
    time.sleep(2)
    quit()
if(__name__ == "__main__"):
    run()
