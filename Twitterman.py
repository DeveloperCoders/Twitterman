# -*- coding: cp1252 -*-
#Created by Lewin
#Developer: developercodersgroup@gmail.com

import pygame, sys,random,easygui,pickle,os



def register():
	name = easygui.enterbox("No players created\nPlease Enter your player name",title="No players found")
	new_player = player(name,1,1)
	with open("data","w") as file:
		pickle.dump(new_player,file)
		file.close()
	return new_player
def dump_level(level,area):
	global new_p
	new_p.level = level
	new_p.area = area
	with open("data", "w") as file:
		pickle.dump(new_p,file)
		file.close()
	
	
###############################################
class player:
	def __init__(self,name,level,area):
		self.level = level
		self.area = area
		self.name = name

	def get_name(self):
		return self.name

	def get_level(self):
		return self.level

	def get_area(self):
		return self.area
###############################################
if os.path.isfile("data"):
	with open("data", "r") as file:
		new_p = pickle.load(file)
		if isinstance(new_p,object):
			pass
		else:
			new_p = register()
else:
	new_p = register()
	
	
j2 = False
pygame.init()
pygame.mixer.init()                  #Sound       
pygame.mixer.music.load("hintergrund_musik.mp3")    #hintergrund_musik
pygame.mixer.music.play(-1)
bild2 = pygame.image.load("k.jpeg")
hintergrund = pygame.image.load('Trump.png')
screen = pygame.display.set_mode([1200,700])
screen.fill([255, 255, 255])
x = 0
pygame.draw.rect(screen, [0,255,0],[1,1,1,51], 0)
pygame.display.flip()
y = 340               #höhe von der Figur
right = True
clock = pygame.time.Clock() 
jump = False
aktiv = True
rand = screen.get_width()
pygame.display.set_caption("Twitterman")
area_colors = {1 : (0,255,0) , 2 : (0,0,255), 3 : (255,0,0), 4 : (0,0,0)}
xk = 350
great = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 355, 360, 365, 370, 375, 380, 385, 390, 395, 400, 405, 410, 415, 420, 425, 430, 435, 440, 445, 450, 455, 460, 465, 470, 475, 480, 485, 490, 495, 500, 505, 510, 515, 520, 525, 530, 535, 540, 545, 550, 555, 560, 565, 570, 575, 580, 585, 590, 595, 600, 605, 610, 615, 620, 625, 630, 635, 640, 645, 650, 655, 660, 665, 670, 675, 680, 685, 690, 695, 700, 705, 710, 715, 720, 725, 730, 735, 740, 745, 750, 755, 760, 765, 770, 775, 780, 785, 790, 795, 800]
yk = 450
itert = 0
count = random.randint(50,70)
lheart = pygame.mixer.Sound("lheart.wav")
points = 0
pofont = pygame.font.Font(None,100)
pf = pofont.render(str(points),1,(255,0,0))
tweet = pygame.image.load("tweet.png")
pygame.display.set_icon(tweet)
bonus = False
level = int(new_p.get_level())
level_re = 5*level
area = int(new_p.get_area())
area_level = area*3
a_color = area_colors[area]
lose = pygame.mixer.Sound("lose.wav")
p2font = pygame.font.Font(None,50)
level_font = p2font.render("Level {0} / Win: {1}".format(level,level_re),1,(255,0,0))
upfont = pygame.font.Font(None,300)
upfont_str = upfont.render("Level UP!",1,(0,255,0))
long_time = 80
long_count = 0
lives = 3
showup = False
live_image = pygame.image.load("lives.png")
level_sound = pygame.mixer.Sound("leveup.wav")
while aktiv:
    clock.tick(70)
    screen.fill([246, 246, 246])
    screen.blit(bild2,[xk,yk])
    if bonus:
   	 screen.blit(tweet,[x+90,y-70])
    screen.blit(pf,[20,20])
    screen.blit(level_font,[800,20])
    for i in range(lives):
	screen.blit(live_image,[400+(i*40),20])
    itert += 1
    if showup:
	screen.blit(upfont_str,[150,200])
	long_count += 1
	if long_count == long_time:
		showup = False
		long_count = 0
    if itert == count:
	xk = random.choice(great)
	xk = random.choice(great)
	count = random.randint(300,500)
	itert = 0

	
    
    if right:
        x += 5
    else:
        x -= 5
    screen.blit(hintergrund, [x,y])
    pygame.draw.rect(screen, a_color,[1,560,1200,5000], 0)            #Rechteck
    if right:
        if x >= 1150:
            x = -300
    else:
        if x == -300:
            x = int(rand)
    pygame.time.delay(5)    #Schnelligeit von der person
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
	    dump_level(level,area)
            aktiv = False
	    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
		if not jump and not j2:
                	jump = True
            elif event.key == pygame.K_d:
                right = True
            elif  event.key == pygame.K_a:
                right = False


    if xk == x and y >= 220:
	if not bonus:
		lives -= 1
		lheart.play()
		if lives == 0:
		
			theend = True
			font_end = pygame.font.Font(None,200)
			p = pygame.font.Font(None,100)
			rendert = font_end.render("Game Over", 1,(255,0,0))
			press = p.render("Press r to play again",1,(255,0,0))
			screen.blit(rendert,[200,130])
			screen.blit(press,[100,260])
			pygame.display.flip()
			while theend:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit(0)
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_r:
							xk = random.choice(great)
							points = 0
							pf = pofont.render(str(points),1,(255,0,0))
							lives = 3
							theend = False
	
						
    elif xk == x+70 and y >= 220:
	if not bonus:
		lives -= 1
		lheart.play()
		if lives == 0:
			
			theend = True
			font_end = pygame.font.Font(None,200)
			p = pygame.font.Font(None,100)
			rendert = font_end.render("Game Over", 1,(255,0,0))
			press = p.render("Press r to play again",1,(255,0,0))
			screen.blit(rendert,[200,130])
			screen.blit(press,[100,260])
			pygame.display.flip()
			while theend:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit(0)
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_r:
							xk = random.choice(great)
							points = 0
							pf = pofont.render(str(points),1,(255,0,0))
							lives = 3
							theend = False
		
					
    elif x == xk:
	points += 1
	if bonus:
		if points == bonus_time:
			bonus = False
	if points == level_re:
		bonus_time = random.randint(0,8)
		level += 1
		level_re += 5
		showup = True
		level_font = p2font.render("Level {0} / Win: {1}".format(level,level_re),1,(255,0,0))
		bonus = True
		points = 0
		level_sound.play()
		if level == area_level:		
			area += 1
			if area == 5:
				pygame.mixer.music.fadeout(500)
				pygame.time.delay(500)
				for i in range(255,0,-1):
					screen.fill([i,i,i])
					pygame.display.flip()
					pygame.time.delay(3)
				pygame.mixer.music.load("Win.mp3")
				pygame.mixer.music.play()
				win_font = pygame.font.Font(None,120)
				credit_font = pygame.font.Font(None,80)
				youwin = win_font.render("You Win",1,(255,0,0))
				screen.blit(youwin,[400,200])
				developers = credit_font.render("Developers: Lewin Sorg & Silas Martini",1,(0,0,255))
				screen.blit(developers,[70,295])
				pygame.display.flip()
				os.unlink("data")
				while True:
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							sys.exit(0)
			else:
				area_level = area+5
				a_color = area_colors[area]
			

		
	pf = pofont.render(str(points),1,(255,0,0))


	
    if jump:
        y -= 10
        if y == 0:
            j2 = True
            jump=False
    if j2:
        y += 10
        if y == 340:
            j2 = False

pygame.quit()

#Created by Lewin
