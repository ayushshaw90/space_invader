import pygame, random, math, time
#initialize pygame
pygame.init()
#create a screen
screen= pygame.display.set_mode((800,600))

#background
background=pygame.image.load('background.png')


#Title of window
pygame.display.set_caption("Space Invaders")
icon =pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#score
score=0

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change=0
playerY_change=0

def player(x,y):
    screen.blit(playerImg, (x,y))

#enemy
enemyImg = pygame.image.load('enemy.png')
no_of_enemies=3
enemyX=[]
enemyY=[]
enemyX_change=[]
for i in range(no_of_enemies):
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
enemyY_change=40


def enemy(x,y):
    screen.blit(enemyImg, (x,y))

#bullet
# ready- you cant see the bullet
# fire- the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change=0
bulletY_change=10
bullet_state = "ready"  

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16,y+10))

#collission
def isCollission(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow((enemyX-bulletX),2)+math.pow((enemyY-bulletY),2))
    if distance < 27:
        return True
    else:
        return False


#game loop
running = True
while running:
    time.sleep(0.002)
    #background
    screen.blit(background,(0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        #If keystroke is pressed check whether is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change-=5
            elif event.key == pygame.K_RIGHT:
                playerX_change+=5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)

        if event.type== pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change=0
    
    #bullet_movement
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change

    if bulletY<0:
        bullet_state="ready"
        bulletY=480

    #collission
    for i in range(no_of_enemies):
        collission=isCollission(enemyX[i],enemyY[i],bulletX,bulletY)
        if collission:
            bullet_state="ready"
            bulletY=480
            score+=1
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)
            print(score)

    #updating the change in coordinates of the player
    playerX=playerX+playerX_change
    if playerX<0:
        playerX=0
    if playerX>736:
        playerX=736
    player(playerX,playerY)
    for i in range(no_of_enemies):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<0:
            enemyX[i]=0
            enemyX_change[i]*=-1
            enemyY[i]+=enemyY_change
        if enemyX[i]>736:
            enemyX[i]=736
            enemyX_change[i]*=-1
            enemyY[i]+=enemyY_change
        
        enemy(enemyX[i],enemyY[i])

    pygame.display.update()
