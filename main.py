import pygame
import random
import time

pygame.init()

# Skärmstorlek
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Arbetsminnesträning")

# Import helper functions and colors
from helpers import draw_text, show_instructions, WHITE, BLACK, RED

def main_menu():
    running = True
    while running:
        screen.fill(BLACK)
        draw_text(screen, "Arbetsminnesspel", 280, 100)
        draw_text(screen, "Tryck på Enter för att starta", 200, 300)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return True

# Import game modules in the desired order
from minnes_vaxling import minnes_vaxling
from n_back import n_back
from objekt_matching import objekt_matching
from sifferspan import sifferspan
from visuellt_span import visuellt_span

def main():
    if main_menu():
        score1 = 0 #minnes_vaxling(screen)
        score2 = 0 #n_back(screen)
        score3 = objekt_matching(screen)
        score4 = sifferspan(screen)
        score5 = visuellt_span(screen)
        total = score1 + score2 + score3 + score4 + score5 # type: ignore

        # Display summary screen
        screen.fill(BLACK)
        draw_text(screen, f"Minnevaxling: {score1}", 250, 100)
        draw_text(screen, f"N-Back: {score2}", 250, 160)
        draw_text(screen, f"Objekt Matching: {score3}", 250, 220)
        draw_text(screen, f"Sifferspan: {score4}", 250, 280)
        draw_text(screen, f"Visuellt Span: {score5}", 250, 340)
        draw_text(screen, f"Total Score: {total}", 250, 400)
        draw_text(screen, "Tryck Enter för att avsluta", 200, 460)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False

if __name__ == '__main__':
    main()
