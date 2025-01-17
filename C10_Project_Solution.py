import pygame

# Initialize pygame
pygame.init()

# Set up display
WINDOW_SIZE = 600
display = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Draw 'S' with Rectangles")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Detect window close
            running = False

    # Fill the screen with a white background
    display.fill(("red"))
    
    # Draw the letter "S" using rectangles
    pygame.draw.rect(display, (0, 0, 0), (200, 150, 100, 20))  # Top bar
    pygame.draw.rect(display, (0, 0, 0), (200, 170, 20, 60))  # Top vertical
    pygame.draw.rect(display, (0, 0, 0), (200, 230, 100, 20))  # Middle bar
    pygame.draw.rect(display, (0, 0, 0), (280, 250, 20, 60))  # Bottom vertical
    pygame.draw.rect(display, (0, 0, 0), (200, 310, 100, 20))  # Bottom bar

    # Update display
    pygame.display.flip()

pygame.quit()
