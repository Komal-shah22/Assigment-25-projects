import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Load player
player_img = pygame.image.load("player.png")  # Replace with your image
player_x = 370
player_y = 480
player_x_change = 0

# Load enemy
enemy_img = pygame.image.load("enemy.png")  # Replace with your image
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 4
enemy_y_change = 40

# Load bullet
bullet_img = pygame.image.load("bullet.png")  # Replace with your image
bullet_x = 0
bullet_y = 480
bullet_y_change = 10
bullet_state = "ready"  # "ready" - you can't see the bullet, "fire" - moving

# Score
score = 0
font = pygame.font.Font(None, 36)

# Welcome message
print("\n~~~~~~ WELCOME TO SPACE INVADERS ~~~~~~")
print("Destroy the aliens and protect the Earth!\n")

def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    return distance < 27

# Game loop
running = True
while running:
    screen.fill((0, 0, 64))  # Background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_x_change = 0

    # Player movement
    player_x += player_x_change
    player_x = max(0, min(player_x, 736))

    # Enemy movement
    enemy_x += enemy_x_change
    if enemy_x <= 0 or enemy_x >= 736:
        enemy_x_change *= -1
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Collision
    if is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
        bullet_y = 480
        bullet_state = "ready"
        score += 1
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 150)

    # Drawing
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # Show score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
