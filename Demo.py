import pygame
pygame.init()

pygame.display.set_caption("RPS-Recognition")

#import image
bg = [pygame.image.load('bg/bgs0.png'),pygame.image.load('bg/bgs1.png'),pygame.image.load('bg/bgs2.png'),pygame.image.load('bg/bgs3.png'),pygame.image.load('bg/bgs4.png'),pygame.image.load('bg/bgs5.png')]

riding_1 = pygame.image.load('Riding_0-22/p1_0.png')

riding_2 = pygame.image.load('Riding_0-22/p2_0.png')

wheelie_1 = [pygame.image.load('Wheelie_23-45/p1_30.png'),pygame.image.load('Wheelie_23-45/p1_31.png'),pygame.image.load('Wheelie_23-45/p1_32.png'),pygame.image.load('Wheelie_23-45/p1_33.png'),pygame.image.load('Wheelie_23-45/p1_34.png'),
pygame.image.load('Wheelie_23-45/p1_35.png'),pygame.image.load('Wheelie_23-45/p1_36.png'),pygame.image.load('Wheelie_23-45/p1_37.png'),pygame.image.load('Wheelie_23-45/p1_38.png'),pygame.image.load('Wheelie_23-45/p1_39.png'),pygame.image.load('Wheelie_23-45/p1_40.png'),
pygame.image.load('Wheelie_23-45/p1_41.png'),pygame.image.load('Wheelie_23-45/p1_42.png'),pygame.image.load('Wheelie_23-45/p1_43.png'),pygame.image.load('Wheelie_23-45/p1_44.png'),pygame.image.load('Wheelie_23-45/p1_45.png')]

wheelie_2 = [pygame.image.load('Wheelie_23-45/p2_30.png'),pygame.image.load('Wheelie_23-45/p2_31.png'),pygame.image.load('Wheelie_23-45/p2_32.png'),pygame.image.load('Wheelie_23-45/p2_33.png'),pygame.image.load('Wheelie_23-45/p2_34.png'),
pygame.image.load('Wheelie_23-45/p2_35.png'),pygame.image.load('Wheelie_23-45/p2_36.png'),pygame.image.load('Wheelie_23-45/p2_37.png'),pygame.image.load('Wheelie_23-45/p2_38.png'),pygame.image.load('Wheelie_23-45/p2_39.png'),pygame.image.load('Wheelie_23-45/p2_40.png'),
pygame.image.load('Wheelie_23-45/p2_41.png'),pygame.image.load('Wheelie_23-45/p2_42.png'),pygame.image.load('Wheelie_23-45/p2_43.png'),pygame.image.load('Wheelie_23-45/p2_44.png'),pygame.image.load('Wheelie_23-45/p2_45.png')]

riding_1 = pygame.transform.scale(riding_1, (riding_1.get_width()//10, riding_1.get_height()//10))
riding_2 = pygame.transform.scale(riding_2, (riding_2.get_width()//10, riding_2.get_height()//10))
for i in range(16):
    wheelie_1[i] = pygame.transform.scale(wheelie_1[i], (wheelie_1[i].get_width()//10, wheelie_1[i].get_height()//10))
    wheelie_2[i] = pygame.transform.scale(wheelie_2[i], (wheelie_2[i].get_width()//10, wheelie_2[i].get_height()//10))

rolling_1 = [pygame.image.load('RPS/Rock_1.png'),pygame.image.load('RPS/Paper_1.png'),pygame.image.load('RPS/Scissors_1.png')]
rolling_2 = [pygame.image.load('RPS/Rock_2.png'),pygame.image.load('RPS/Paper_2.png'),pygame.image.load('RPS/Scissors_2.png')]
for i in range(3):
    rolling_1[i] = pygame.transform.scale(rolling_1[i], (rolling_1[i].get_width()+60, rolling_1[i].get_height()+60))
    rolling_2[i] = pygame.transform.scale(rolling_2[i], (rolling_2[i].get_width()+60, rolling_2[i].get_height()+60))

#OOP
class rider(object):
    def __init__(self, x, y, width, height, image, wheelie):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.vel = 0
        self.wheeling = False
        self.wheelcnt = 0
        self.maxspeed = 18
        self.wheelie = wheelie
        self.temp = image
        self.tempvel = self.vel
        self.tempwheel = 31
    
    def draw(self, win):
        if self.wheelcnt > 15:
            self.tempwheel = 15
        else:
            self.tempwheel = self.wheelcnt
            if self.tempvel < self.vel and self.wheeling:
                self.vel -= 1

        if not(self.wheeling):
            self.temp = self.image
        else:
            self.temp = self.wheelie[self.tempwheel]
            self.wheeler()
        self.autorun()
        win.blit(self.temp, (self.x, self.y+motor))

    def autorun(self):
        if self.x >= 1140 and self.vel > 0:
            self.vel -= 1
        self.x += self.vel

    def wheeler(self):
        if self.wheelcnt > 0:
            self.wheelcnt -= 1
        else:
            self.wheeling = False
            self.wheelcnt = 31
    
    #Old Function at the beginning
    def KeyControl(self, keys, left, right):
        if keys[left] and self.x > 2:
            self.x -= self.vel
        elif keys[right] and self.x < 1280-self.width:
            self.x += self.vel

    def WheelControl(self, keys, whee):
        if keys[whee]:
            self.wheeling = True
            self.wheelcnt = 15
            if self.vel < self.maxspeed:
                self.vel += 1
        else:
            if self.vel > 5:
                self.vel -= 1

        if self.wheelcnt == 0:
            self.wheeling = False
        if self.wheelcnt > 0 and self.wheeling:
            self.wheelcnt -= 1

class roll(object):
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.cnt = 0
        self.result = 0
        self.temp = image
        self.streak = 0

    def draw(self, win, cooldown):
        if cooldown > 0:
            self.temp = self.image[self.result]
        else:
            self.rolling(win)
            self.temp = self.image[self.cnt]
        win.blit(self.temp, (self.x, self.y))

    def rolling(self, win):
        self.cnt += 1
        if self.cnt == 3:
            self.cnt = 0

    def setResult(self, res):
        self.result = res

#Animation
def redrawGameWindow():
    global daytime, motor, running 
    win.blit(bg[(int)(daytime/500)] ,(0,0))
    rider_1.draw(win)
    rider_2.draw(win)
    if running:
        roll_1.draw(win, cooldown)
        roll_2.draw(win, cooldown)

    if daytime+1 > 2500:
        daytime = 0

    daytime += 1
    if(daytime%2==0):
        motor *= -1

    # Check Error
    if rider_1.wheeling:
        win.blit(textsurface1,(0,0))
    if rider_1.vel > 6:
        win.blit(textsurface2,(555,0))
    if roll_1.streak > 2:
        win.blit(textsurface3,(555,80))
    pygame.display.update()

#Objects
win = pygame.display.set_mode((1280, 720))
rider_1 = rider(50, 560, 50, 50, riding_1, wheelie_1)
rider_2 = rider(50, 640, 50, 50, riding_2, wheelie_2)
roll_1 = roll(370, 250, rolling_1)
roll_2 = roll(750, 250, rolling_2)

#Setting FPS
clock = pygame.time.Clock()

#Variables
black = ( 0, 0, 0)
daytime = 0
motor = -2
running = False
space = False
cooldown = 0

#Font
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

textsurface1 = myfont.render('wheeling', False, black)
textsurface2 = myfont.render('vel more 6', False, black)
textsurface3 = myfont.render('streak more 2', False, black)

#main loop
run = True
while run: 
    clock.tick(30)#FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    #Start and pause game (For test)
    if keys[pygame.K_SPACE]:
        if space == False:
            if running == True:
                running = False
            else:
                running = True
        space = True
    else: 
        space = False
    
    #win condition
    if keys[pygame.K_x]:
        if cooldown == 0:
            roll_1.streak += 1
            if roll_1.streak > 2:
                #wheeling ติดตรงนี้นะ พอชนะได้ streak = 3 มันได้ความเร็ว แต่ไม่ได้ยกล้อ
                rider_1.wheeling = True
                rider_1.tempvel = rider_1.vel 
                rider_1.vel = 7
            else:
                roll_1.setResult(0)
                roll_2.setResult(2)
                rider_1.vel += 1
            cooldown = 45

    if keys[pygame.K_c]:
        if cooldown == 0:
            roll_2.streak += 1
            if roll_2.streak > 2:
                #wheeling
                rider_2.wheeling = True
                rider_2.tempvel = rider_2.vel
                rider_2.vel = 7
            else:
                roll_1.setResult(2)
                roll_2.setResult(0)
                rider_2.vel += 1
            cooldown = 45

    if keys[pygame.K_v]:
        if cooldown == 0:
            roll_1.setResult(1)
            roll_2.setResult(1)
            roll_1.streak = 0
            roll_2.streak = 0
        cooldown = 45

    if cooldown > 0:
        cooldown -= 1
        
    if keys[pygame.K_z]:
        rider_1.x = 50
        rider_2.x = 50
        rider_1.vel = 0
        rider_2.vel = 0
    redrawGameWindow()    

pygame.quit()

