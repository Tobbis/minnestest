import pygame, random
from helpers import draw_text, show_instructions, BLACK
import time

def minnes_vaxling(screen):
    if not show_instructions(screen, [
        "Minnesväxling:",
        "Växla mellan två regler:",
        "Siffra: Vänster = jämn, Höger = udda",
        "Bokstav: Upp = vokal, Ner = konsonant",
        "Svara snabbt och korrekt!"
    ]):
        return 0

    score = 0
    rounds = 10
    vowels = "AEIOUY"
    consonants = "BCDFGHJKLMNPQRSTVWXZ"

    for _ in range(rounds):
        screen.fill(BLACK)
        is_number = random.choice([True, False])

        if is_number:
            item = str(random.randint(0, 9))
            correct_key = pygame.K_LEFT if int(item) % 2 == 0 else pygame.K_RIGHT
        else:
            item = random.choice(vowels + consonants)
            correct_key = pygame.K_UP if item in vowels else pygame.K_DOWN

        draw_text(screen, item, 380, 250)
        pygame.display.flip()

        start_time = time.time()
        responded = False

        while time.time() - start_time < 2:  # Svara inom 2 sekunder
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == correct_key:
                        score += 1
                        responded = True
                    responded = True
            if responded:
                break

    return score

# Removed pygame.quit() so that the display remains active
