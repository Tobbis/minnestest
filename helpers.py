import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
# Ändrad fontstorlek från 50 till 40
font = pygame.font.Font(None, 40)

def draw_text(screen, text, x, y, color=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def show_instructions(screen, text_lines):
    screen.fill(BLACK)
    y_offset = 200
    for line in text_lines:
        draw_text(screen, line, 100, y_offset)
        y_offset += 50
    draw_text(screen, "Tryck på Enter för att börja", 200, y_offset + 50)
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True
