import pygame
import math
import random

pygame.init()

from pygame.locals import *
from pygame import mixer
# Create the screen
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('rocket.png')
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(icon)



# Background
background = pygame.image.load('background.png')
mixer.music.load('background.wav')
mixer.music.play(-1)
# Player
PlayerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
number_of_enemies = 6
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
for i in range(number_of_enemies):
    EnemyImg.append( pygame.image.load('enemy.png'))
    EnemyX.append(random.randint(0, 735))
    EnemyY.append(random.randint(50, 75))
    EnemyX_change.append(6)
    EnemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 8
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#Game over Text
over_game = pygame.font.Font('freesansbold.ttf', 64)

press_Enter = pygame.font.Font('freesansbold.ttf', 20)

def show_score(x , y):
    global number_of_enemies
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    run = True
    while run :
        game_over = over_game.render("Game Over", True, (255,255,255))
        screen.blit(game_over, (200, 250))
        Enter_Key = press_Enter.render("Please press Enter_Key to Start New Game ", True, (255,255,255))
        screen.blit(Enter_Key, (200, 400))
        pygame.display.update()
        for events in pygame.event.get():
            if events.type == KEYDOWN:
                if events.key == K_RETURN:
                    run = False
                    break


def enemy(x, y, i):
    screen.blit(EnemyImg[i], (EnemyX[i], EnemyY[i]))


def player(x, y):
    screen.blit(PlayerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def iscollision(bulletX, bulletY, enemyX, enemyY,):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
        
        if events.type == KEYDOWN:
            if events.key == K_SPACE:
                if bullet_state == "ready":
                    Bullet_sound = mixer.Sound('laser.wav')
                    Bullet_sound.play()
                    mixer.Sound
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
    if events.type == KEYDOWN:
        if events.key == K_LEFT:
                playerX_change = -9
        if events.key == K_RIGHT:
            playerX_change = 9
            

    if events.type == pygame.KEYUP:
        if events.key == pygame.K_LEFT or events.key == pygame.K_RIGHT:
            playerX_change = 0
    playerX += playerX_change

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    if playerY <= 36:
        playerY = 36
    elif playerY >= 536:
        playerY = 536

    for i in range(number_of_enemies):
    # Enemy Movement
        if EnemyY[i] > 440:
            for j in range(number_of_enemies):
                EnemyY[j] = 200
            game_over_text()
            score_value = 0
            break


        EnemyX[i] += EnemyX_change[i]

        if EnemyX[i] <= 0:
            EnemyX_change[i] = 8
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -8
            EnemyY[i] += EnemyY_change[i]
        collision = iscollision(bulletX, bulletY, EnemyX[i], EnemyY[i])
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            score_value += 1
            bullet_state = "ready"
            bulletY = 480
            EnemyX[i] = random.randint(0, 735)
            EnemyY[i] = random.randint(50, 75)
        enemy(EnemyX_change[i], EnemyY_change[i], i)
    
    playerY += playerY_change

    # Bullet movement
    if bullet_state == "fire":
        bulletY -= bulletY_change
    
    

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
