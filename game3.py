import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Shooting Game")
clock = pygame.time.Clock()

# Player variables
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2 - player_width // 2, HEIGHT - player_height - 20
player_speed = 7

# Bullet variables
bullet_width, bullet_height = 5, 15
bullet_speed = 10
bullets = []

# Target variables
target_width, target_height = 50, 50
target_x, target_y = WIDTH // 2 - target_width // 2, HEIGHT // 2 - target_height // 2
target_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_y = player_y
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move bullets
    for bullet in bullets:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

        # Check collision with target
        if bullet.colliderect(pygame.Rect(target_x, target_y, target_width, target_height)):
            bullets.remove(bullet)
            score += 1
            target_x = pygame.time.get_ticks() % (WIDTH - target_width)

    # Move target
    target_x += target_speed
    if target_x > WIDTH - target_width or target_x < 0:
        target_speed *= -1

    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    # Draw target
    pygame.draw.rect(screen, BLACK, (target_x, target_y, target_width, target_height))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)
