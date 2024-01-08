import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")
clock = pygame.time.Clock()

# Player variables
player_width, player_height = 40, 60
player_x, player_y = WIDTH // 2 - player_width // 2, HEIGHT // 2 - player_height // 2
player_speed = 5
is_jumping = False
jump_count = 10

# Platform variables
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
    pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2, 100, 20)
]

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
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Jumping mechanics
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Update player rectangle
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Draw player
    pygame.draw.rect(screen, BLACK, player_rect)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

    pygame.display.flip()
    clock.tick(FPS)
