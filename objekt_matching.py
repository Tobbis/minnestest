import pygame, random, time
from helpers import draw_text, show_instructions, BLACK

def objekt_matching(screen):
    if not show_instructions(screen, [
        "Objekt Matching:",
        "Matcha objekt som visas på skärmen.",
        "Tryck på motsvarande tangent."
    ]):
        return 0

    score = 0
    shapes = ['O', 'X', '△']
    target = random.choice(shapes)
    screen.fill(BLACK)
    draw_text(screen, target, 380, 250)
    pygame.display.flip()
    time.sleep(2)
    draw_text(screen, "Tryck O, X eller △", 280, 350)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:
                if event.unicode == target:
                    score = 1
                return score
