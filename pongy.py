import pygame
import sys

pygame.init()
pygame.mixer.init()
#Text
p1score = 0
p2score = 0
game_font = pygame.font.Font("freesansbold.ttf", 40)
#audio
hitsound = 'hit.mp3'
scoresound = 'score.mp3'


#Ball
def ballmovement():
    global ballspx
    global ballspy
    global p1score
    global p2score
    ball.x += ballspx
    ball.y += ballspy
    if ball.top <= 0 or ball.bottom >= winh:
        ballspy *= -1
    if ball.left <= 0:
        p2score +=1
        ballstart()
        ballspx *= -1
        ballspy *= -1
    elif ball.right >= winw:
        p1score +=1
        ballstart()
        ballspx *= -1
        ballspy *= -1    
    if ball.colliderect(p1):
        ballspx *= -1
    if ball.colliderect(p2):  
        ballspx *= -1

def ballstart():
    ball.x = 300
    ball.y = 200
    
#Window


clock = pygame.time.Clock()
back = (40,19,13)
winw , winh = 600, 400
win = pygame.display.set_mode((winw, winh))
pygame.display.set_caption('2Player-Pong')
win.fill(back)

#vars
ballx = 285
bally = 200 
MColor = (252,255,128)
y1 = 150
y2 = 150
width = 15
height = 100
p1vel = 0
p2vel = 0

#Players
p1 = pygame.Rect(0, y1, width, height)
p2 = pygame.Rect(winw - width, y2, width, height)
#Ball
ball = pygame.Rect(winw/2 - 15, winh/2 - 15, 15, 15)
ballspx = 5.75
ballspy = 5.75
#Line
line = pygame.Rect(295, 0, 5, 400)

#GamelOop
run = True

while run:
    
    
    
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1vel -= 5
            if event.key == pygame.K_s:
                p1vel += 5
            if event.key == pygame.K_UP:
                p2vel -= 5
            if event.key == pygame.K_DOWN:
                p2vel += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1vel +=5
            if event.key == pygame.K_s:
                p1vel -=5
            if event.key == pygame.K_UP:
                p2vel +=5
            if event.key == pygame.K_DOWN:
                p2vel -=5
            
    

    
    ballmovement()
    p1.y += p1vel
    p2.y += p2vel
    if p1.top <=0:
        p1.top = 0
    if p1.bottom >=winh:
        p1.bottom = winh
    if p2.top <=0:
        p2.top = 0
    if p2.bottom >=winh:
        p2.bottom = winh
    #drawing
    pygame.draw.rect(win, MColor, line)
    pygame.draw.ellipse(win, MColor, ball )
    pygame.draw.rect(win, MColor, p1)
    pygame.draw.rect(win, MColor, p2)
    p1text = game_font.render(f"{p1score}",True,MColor)
    win.blit(p1text,(130,25))
    p2text = game_font.render(f"{p2score}",True, MColor)
    win.blit(p2text,(450,25))
    pygame.display.update()
    clock.tick(60)
    win.fill(back)
pygame.quit()
sys.exit()