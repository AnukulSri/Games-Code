import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Shooting Game")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
player_size = 50
player_speed = 5
bubble_radius = 20
bubble_speed = 3
bubbles = []
score = 0

# Player
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT - 2 * player_size, player_size, player_size)

# Function to create new bubble
def create_bubble():
    x = random.randint(bubble_radius, WIDTH - bubble_radius)
    y = random.randint(-2 * bubble_radius, -bubble_radius)
    return pygame.Rect(x, y, 2 * bubble_radius, 2 * bubble_radius)

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Shooting bubbles
    if keys[pygame.K_SPACE]:
        new_bubble = create_bubble()
        bubbles.append(new_bubble)

    # Move and draw bubbles
    for bubble in bubbles:
        pygame.draw.circle(screen, BLUE, bubble.center, bubble_radius)
        bubble.y += bubble_speed

        # Collision check
        if bubble.colliderect(player):
            bubbles.remove(bubble)
            score += 1

        if bubble.top > HEIGHT:
            bubbles.remove(bubble)

    # Draw player
    pygame.draw.rect(screen, RED, player)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)
