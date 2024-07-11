import pygame
import random
import sys

pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Game variables
score = 0
lives = 3

# Player variables
basket_width = 100
basket_height = 50
basket_x = SCREEN_WIDTH // 2 - basket_width // 2
basket_y = SCREEN_HEIGHT - basket_height - 10
basket_speed = 10

# Fruit variables
fruit_width = 50
fruit_height = 50
fruit_speed = 5
fruits = []

def create_fruit():
    x = random.randint(0, SCREEN_WIDTH - fruit_width)
    y = -fruit_height
    fruits.append([x, y])

def draw_basket():
    pygame.draw.rect(screen, RED, (basket_x, basket_y, basket_width, basket_height))

def draw_fruits():
    for fruit in fruits:
        pygame.draw.rect(screen, WHITE, (fruit[0], fruit[1], fruit_width, fruit_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player's basket
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - basket_width:
        basket_x += basket_speed

    # Create new fruits
    if len(fruits) < 10:
        create_fruit()

    # Update fruit positions
    for fruit in fruits:
        fruit[1] += fruit_speed

        # Check collision with the basket
        if fruit[1] + fruit_height >= basket_y and basket_x <= fruit[0] <= basket_x + basket_width:
            score += 1
            fruits.remove(fruit)

        # Check if fruit reaches the bottom
        if fruit[1] >= SCREEN_HEIGHT:
            lives -= 1
            fruits.remove(fruit)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player's basket
    draw_basket()

    # Draw the falling fruits
    draw_fruits()

    # Display the score and remaining lives
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    # Update the screen
    pygame.display.flip()
    clock.tick(60)
    `